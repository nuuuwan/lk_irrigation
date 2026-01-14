# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_06:33:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,097 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 06:33:05 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.001 |  |
| 2026-01-14 06:18:39 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:12:48 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-14 06:11:53 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:10:15 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.136 |  |
| 2026-01-14 06:09:11 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:08:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:07:37 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.015 |  |
| 2026-01-14 06:07:06 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:06:19 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 06:06:11 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:06:02 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:05:51 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.136 |  |
| 2026-01-14 06:05:35 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.035 |  |
| 2026-01-14 06:05:22 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-01-14 06:04:37 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-14 06:04:20 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:04:17 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-01-14 06:04:12 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-14 06:03:56 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.045 |  |
| 2026-01-14 06:03:49 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-01-14 06:03:45 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.038 |  |
| 2026-01-14 06:03:43 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.028 |  |
| 2026-01-14 06:03:05 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:03:02 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-01-14 06:03:00 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-14 06:02:53 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:02:42 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-14 06:02:37 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-14 06:02:34 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:02:19 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:02:00 | Horowpothana (Yan Oya) | 3.46 | 🟢 Normal | -180.000 |  |
| 2026-01-14 06:01:59 | Horowpothana (Yan Oya) | 3.51 | 🟢 Normal | -180.000 |  |
| 2026-01-14 06:01:52 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:01:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:00:36 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:00:34 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.032 |  |
| 2026-01-14 06:00:30 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-14 06:00:10 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.203 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 06:02:42 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-14 06:02:37 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-14 06:12:48 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-14 06:06:19 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 06:04:12 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-14 06:00:30 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-14 06:04:37 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-14 06:33:05 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.001 |  |
| 2026-01-14 06:18:39 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:01:08 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:03:05 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:02:53 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:00:36 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:03:43 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:09:11 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:07:06 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:08:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:04:20 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:02:34 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:06:11 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:11:53 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:02:19 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:06:02 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 06:03:00 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-14 06:03:02 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-01-14 06:07:37 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.015 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-14 06:05:22 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-01-14 06:03:49 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-01-14 06:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.028 |  |
| 2026-01-14 06:04:17 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-01-14 06:00:34 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.032 |  |
| 2026-01-14 06:05:35 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.035 |  |
| 2026-01-14 06:03:45 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.038 |  |
| 2026-01-14 06:03:56 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.045 |  |
| 2026-01-14 06:10:15 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.136 |  |
| 2026-01-14 06:00:10 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.203 |  |
| 2026-01-14 06:02:00 | Horowpothana (Yan Oya) | 3.46 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)