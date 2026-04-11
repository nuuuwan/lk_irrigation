# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_13:28:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,182 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 13:28:40 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:27:15 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-04-11 13:21:08 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:20:09 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-04-11 13:13:54 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.078 |  |
| 2026-04-11 13:11:49 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-04-11 13:09:29 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:09:05 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:08:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-04-11 13:08:50 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:08:37 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-11 13:07:50 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:07:42 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:07:33 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-04-11 13:06:39 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-11 13:06:16 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 13:05:58 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.079 |  |
| 2026-04-11 13:05:49 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:04:16 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.013 |  |
| 2026-04-11 13:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-11 13:04:03 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.060 |  |
| 2026-04-11 13:03:49 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:03:30 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.020 |  |
| 2026-04-11 13:03:03 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:56 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.060 |  |
| 2026-04-11 13:02:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:14 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:04 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:04 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:01:57 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 13:01:42 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:01:34 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:01:29 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:01:14 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-11 13:01:10 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-04-11 13:00:49 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.079 |  |
| 2026-04-11 13:00:37 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-04-11 13:00:33 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 13:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-11 13:01:57 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 13:06:16 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 13:00:33 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:04 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:01:42 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:28:40 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:07:50 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:14 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:05:49 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:01:29 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:03:49 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:01:34 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:04 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:03:03 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:07:42 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:08:50 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:09:05 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:09:29 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 13:11:49 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-04-11 13:08:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-04-11 13:01:10 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-04-11 13:06:39 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-11 13:08:37 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-11 13:01:14 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-11 13:04:16 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.013 |  |
| 2026-04-11 13:07:33 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-04-11 13:00:37 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-04-11 13:03:30 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.020 |  |
| 2026-04-11 13:27:15 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-04-11 13:20:09 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-04-11 13:02:56 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.060 |  |
| 2026-04-11 13:04:03 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.060 |  |
| 2026-04-11 13:13:54 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.078 |  |
| 2026-04-11 13:05:58 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.079 |  |
| 2026-04-11 13:00:49 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)