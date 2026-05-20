# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_17:22:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,146 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 17:22:29 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.009 |  |
| 2026-05-20 17:20:03 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-05-20 17:18:31 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:15:43 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:12:07 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.022 |  |
| 2026-05-20 17:11:50 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:11:05 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 17:08:15 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-20 17:07:54 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:06:36 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:06:20 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-20 17:06:15 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-20 17:06:06 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.028 |  |
| 2026-05-20 17:05:29 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 17:04:51 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:04:48 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:04:46 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 17:04:34 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:04:17 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-20 17:03:47 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 17:03:34 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:03:13 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | -0.019 |  |
| 2026-05-20 17:02:52 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:02:51 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-05-20 17:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:02:33 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:02:31 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-05-20 17:02:19 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:02:15 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:01:57 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-20 17:01:32 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:01:11 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:00:57 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:00:44 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-20 17:00:26 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-20 17:00:10 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 17:01:57 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-20 17:04:17 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-20 17:00:26 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-20 16:04:43 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-20 17:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-20 17:05:29 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 17:03:47 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 17:04:46 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 17:11:05 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 17:08:15 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-20 16:01:22 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:01:32 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:02:52 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:06:36 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:03:34 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:00:44 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:11:50 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:18:31 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:02:15 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:02:33 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:01:11 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:04:34 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:04:51 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:02:19 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:07:54 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:15:43 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:04:48 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:00:57 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:00:10 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | 0.000 |  |
| 2026-05-20 17:22:29 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.009 |  |
| 2026-05-20 17:20:03 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-05-20 17:06:15 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-20 17:06:20 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-20 17:03:13 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | -0.019 |  |
| 2026-05-20 17:02:51 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-05-20 17:02:31 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-05-20 17:12:07 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.022 |  |
| 2026-05-20 17:06:06 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.028 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)