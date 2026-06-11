# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_11:12:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,405 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 11:12:43 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 11:11:37 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-11 11:08:04 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:07:39 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 11:07:32 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 11:06:50 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-11 11:06:33 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 11:06:02 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:05:59 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 11:05:38 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:05:20 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 11:05:18 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-06-11 11:04:47 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 11:04:36 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:04:34 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.015 |  |
| 2026-06-11 11:04:01 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:03:56 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-11 11:03:44 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 11:03:39 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 11:03:28 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:03:24 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-11 11:03:12 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 11:02:52 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-06-11 11:02:47 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-11 11:02:42 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-11 11:02:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:02:30 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-11 11:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 11:02:21 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:01:35 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-11 11:01:19 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 11:01:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-06-11 11:01:08 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-11 11:01:04 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:00:49 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:00:38 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:00:32 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:00:15 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 11:06:50 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-11 11:02:42 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-11 11:02:47 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-11 11:11:37 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-11 11:02:30 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-11 11:04:47 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 11:07:39 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 11:01:08 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-11 11:12:43 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 11:03:39 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 11:01:19 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 11:05:20 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 11:03:44 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 11:07:32 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 11:06:33 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 11:05:59 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 11:03:12 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 11:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 11:04:36 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:01:04 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:00:15 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:00:38 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:02:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:02:21 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:06:02 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:03:28 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:01:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:04:01 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:08:04 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:05:38 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:00:49 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-11 11:03:24 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-11 11:03:56 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-11 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-06-11 11:01:35 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-11 11:05:18 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-06-11 11:04:34 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.015 |  |
| 2026-06-11 11:02:52 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)