# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_03:02:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,540 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 03:02:29 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-28 03:02:23 | Glencourse (Kelani Ganga) | 12.40 | 🟢 Normal | -0.088 |  |
| 2026-05-28 03:02:18 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-28 03:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.57 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-05-28 03:02:08 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 03:02:02 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-28 03:02:01 | Thawalama (Gin Ganga) | 3.37 | 🟢 Normal | -0.052 |  |
| 2026-05-28 03:01:42 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-28 03:01:29 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.061 |  |
| 2026-05-28 03:01:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 03:01:10 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 03:00:34 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-28 02:57:34 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 02:21:02 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-28 02:16:41 | Rathnapura (Kalu Ganga) | 4.87 | 🟢 Normal | -0.061 |  |
| 2026-05-28 02:14:43 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-05-28 02:12:45 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 03:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.57 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-05-28 02:14:43 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-05-28 03:02:02 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-27 18:00:23 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-28 01:07:37 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 00:07:50 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-28 03:02:29 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-28 02:21:02 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-28 02:01:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 02:07:58 | Hanwella (Kelani Ganga) | 4.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 02:07:12 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-28 01:05:52 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-28 03:01:42 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-28 03:01:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 02:03:35 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-28 02:57:34 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 00:06:13 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-28 02:04:10 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-28 02:02:51 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 02:12:45 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 03:02:08 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 03:01:10 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 02:06:31 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 03:00:34 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-28 02:01:41 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-28 02:05:18 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:05:39 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-28 02:03:52 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-05-28 02:01:27 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-05-28 03:02:18 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-28 03:02:01 | Thawalama (Gin Ganga) | 3.37 | 🟢 Normal | -0.052 |  |
| 2026-05-28 02:07:50 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-05-28 02:16:41 | Rathnapura (Kalu Ganga) | 4.87 | 🟢 Normal | -0.061 |  |
| 2026-05-28 03:01:29 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.061 |  |
| 2026-05-28 02:04:47 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.066 |  |
| 2026-05-28 03:02:23 | Glencourse (Kelani Ganga) | 12.40 | 🟢 Normal | -0.088 |  |
| 2026-05-28 02:03:16 | Deraniyagala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.119 |  |
| 2026-05-28 02:03:15 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)