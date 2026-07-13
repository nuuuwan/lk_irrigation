# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_12:03:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,082 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 12:03:27 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:03:19 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:03:16 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.040 |  |
| 2026-07-13 12:02:48 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:42 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:41 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-07-13 12:02:38 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:35 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:33 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-07-13 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:12 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:08 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 12:02:06 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:00 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-07-13 12:01:57 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-13 12:01:47 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:01:42 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:01:36 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:01:26 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:01:22 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:01:18 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:00:41 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:00:30 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-13 12:00:26 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 11:35:03 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-07-13 11:32:32 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 11:17:55 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.055 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 12:02:00 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-07-13 11:06:53 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-13 11:35:03 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-07-13 12:01:57 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-13 12:00:30 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-13 12:02:08 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 12:00:26 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 11:01:54 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 11:05:36 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 12:01:18 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:01:22 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:01:36 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 11:07:16 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:03:27 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:01:42 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:03:16 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:12 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:01:26 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:38 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:03:19 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:48 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 11:01:50 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-13 11:02:13 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-13 11:05:26 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:06 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:00:41 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 11:04:15 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:35 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:42 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:01:47 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-07-13 11:06:14 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-13 12:02:33 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-07-13 11:04:08 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-07-13 11:02:00 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-07-13 12:02:41 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-07-13 11:02:58 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-07-13 12:02:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)