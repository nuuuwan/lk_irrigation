# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_10:21:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,629 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 10:21:54 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:17:13 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:12:07 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-15 10:11:10 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-04-15 10:09:03 | Kithulgala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.176 |  |
| 2026-04-15 10:08:10 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-15 10:08:08 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -18.000 |  |
| 2026-04-15 10:08:06 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -18.000 |  |
| 2026-04-15 10:07:24 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-04-15 10:06:57 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.018 |  |
| 2026-04-15 10:06:05 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-15 10:05:27 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:05:12 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.051 |  |
| 2026-04-15 10:03:38 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:03:29 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-04-15 10:03:24 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:03:10 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:03:09 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-15 10:03:06 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-04-15 10:03:05 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-15 10:03:05 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 10:03:02 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.043 |  |
| 2026-04-15 10:02:52 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-15 10:02:48 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-15 10:02:40 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:02:38 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-15 10:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.040 |  |
| 2026-04-15 10:02:17 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-04-15 10:02:16 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:02:08 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:01:57 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.041 |  |
| 2026-04-15 10:01:51 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-15 10:00:55 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-15 10:00:53 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-15 10:00:50 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-15 10:00:33 | Thanthirimale (Malwathu Oya) | 2.70 | 🟢 Normal | -0.041 |  |
| 2026-04-15 10:00:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:00:10 | Weraganthota (Mahaweli Ganga) | -2.43 | 🟢 Normal | 0.311 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 10:00:10 | Weraganthota (Mahaweli Ganga) | -2.43 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-04-15 10:02:48 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-15 10:00:50 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-15 10:02:38 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-15 10:00:55 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-15 10:12:07 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-15 10:03:05 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 10:08:10 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-15 10:00:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:05:27 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-15 09:19:11 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:17:13 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:21:54 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:03:10 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:02:08 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:03:38 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:05:12 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:02:16 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:03:24 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:02:40 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-15 10:11:10 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-04-15 10:06:05 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-15 10:02:52 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-15 10:03:05 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-15 10:03:09 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-15 10:02:17 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-04-15 10:06:57 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.018 |  |
| 2026-04-15 10:01:51 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-15 10:00:53 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-15 10:03:06 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-04-15 10:07:24 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-04-15 10:03:29 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-04-15 10:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.040 |  |
| 2026-04-15 10:00:33 | Thanthirimale (Malwathu Oya) | 2.70 | 🟢 Normal | -0.041 |  |
| 2026-04-15 10:01:57 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.041 |  |
| 2026-04-15 10:03:02 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.043 |  |
| 2026-04-15 10:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.051 |  |
| 2026-04-15 10:09:03 | Kithulgala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.176 |  |
| 2026-04-15 10:08:08 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)