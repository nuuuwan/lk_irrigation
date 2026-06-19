# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_23:09:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,991 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 23:09:31 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-06-19 23:09:02 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-06-19 23:08:27 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-06-19 23:08:19 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-06-19 23:07:50 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:07:48 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.039 |  |
| 2026-06-19 23:07:32 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-06-19 23:07:07 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.091 |  |
| 2026-06-19 23:06:10 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-06-19 23:05:43 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-06-19 23:05:35 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:05:08 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.019 |  |
| 2026-06-19 23:03:59 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-06-19 23:03:31 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.020 |  |
| 2026-06-19 23:02:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:02:50 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:02:36 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-06-19 23:02:32 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 23:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | -0.033 |  |
| 2026-06-19 23:02:17 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:02:10 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:01:50 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:01:38 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:01:37 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 23:01:26 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.040 |  |
| 2026-06-19 23:01:14 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-06-19 23:00:30 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:18 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:15 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:11 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 23:01:14 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-06-19 22:06:17 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-19 23:01:37 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-19 23:02:32 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:18 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:30 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:11 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:15 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:02:50 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:02:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:01:38 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:01:50 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:10:39 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:02:17 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:05:35 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:07:50 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:02:10 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-19 20:04:15 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-19 23:08:27 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-06-19 23:03:59 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-06-19 23:02:36 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-19 23:05:43 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-06-19 23:06:10 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-06-19 23:05:08 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.019 |  |
| 2026-06-19 23:07:32 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-06-19 23:08:19 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-06-19 23:03:31 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.020 |  |
| 2026-06-19 23:09:31 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-06-19 22:02:23 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-19 23:09:02 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-06-19 23:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | -0.033 |  |
| 2026-06-19 22:11:20 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.034 |  |
| 2026-06-19 23:07:48 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.039 |  |
| 2026-06-19 23:01:26 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.040 |  |
| 2026-06-19 23:07:07 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)