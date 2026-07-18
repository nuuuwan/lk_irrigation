# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18_09:04:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **209,411 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-18 09:04:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:04:22 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:04:10 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:03:32 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-07-18 09:03:32 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-07-18 09:03:31 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-18 09:03:22 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.106 |  |
| 2026-07-18 09:03:19 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-18 09:03:17 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-18 09:03:16 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-07-18 09:03:12 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:03:09 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:02:56 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.011 |  |
| 2026-07-18 09:02:50 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-07-18 09:02:43 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:02:28 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:01:51 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.034 |  |
| 2026-07-18 09:01:45 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:01:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:01:40 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.013 |  |
| 2026-07-18 09:01:39 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:01:18 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-18 09:01:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:01:06 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:00:46 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:00:22 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:00:13 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-07-18 08:35:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-18 08:21:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -11.368 |  |
| 2026-07-18 08:21:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -11.368 |  |
| 2026-07-18 08:15:54 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-18 09:00:13 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-07-18 09:01:18 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-18 09:03:19 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-18 09:03:31 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-18 09:03:17 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-18 09:03:09 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:00:46 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:04:22 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:01:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-18 08:08:24 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-18 08:01:08 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:04:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 08:03:49 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-18 08:10:53 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:03:12 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-18 08:01:12 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:01:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:04:10 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.000 |  |
| 2026-07-18 08:03:23 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-18 08:03:01 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:02:43 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:01:06 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:01:39 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:01:45 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:00:22 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:02:28 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 09:03:32 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-07-18 09:03:32 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-07-18 09:02:56 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.011 |  |
| 2026-07-18 09:01:40 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.013 |  |
| 2026-07-18 08:07:34 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | -0.014 |  |
| 2026-07-18 08:11:18 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.018 |  |
| 2026-07-18 09:03:16 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-07-18 09:01:51 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.034 |  |
| 2026-07-18 08:02:32 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.059 |  |
| 2026-07-18 09:02:50 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-07-18 09:03:22 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.106 |  |
| 2026-07-18 08:21:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -11.368 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)