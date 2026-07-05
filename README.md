# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_04:03:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,488 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 04:03:30 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-07-06 04:03:19 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:02:49 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:02:29 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-07-06 04:02:26 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-06 04:02:17 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-06 04:01:56 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:01:51 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.084 |  |
| 2026-07-06 04:01:24 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-06 04:01:22 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.020 |  |
| 2026-07-06 04:01:16 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-06 04:01:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:00:48 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:00:44 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:00:34 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 03:33:03 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-07-06 03:21:14 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-07-06 03:18:02 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-07-06 03:17:50 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.008 |  |
| 2026-07-06 03:16:38 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-06 03:15:38 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -3762.000 |  |
| 2026-07-06 03:15:36 | Deraniyagala (Kelani Ganga) | 3.00 | 🟢 Normal | -3762.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 03:08:20 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-07-06 03:33:03 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-07-06 03:16:38 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-06 04:01:24 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-06 03:05:16 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-06 04:02:26 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-06 03:04:44 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-06 04:01:16 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-06 01:05:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 04:00:48 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:00:44 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:00:34 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:03:07 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:01:51 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:41 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:02:49 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-06 03:18:02 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-07-06 03:03:06 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:03:19 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:01:56 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-06 04:01:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 03:03:17 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 03:17:50 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.008 |  |
| 2026-07-06 03:21:14 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-07-06 04:02:17 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 03:06:02 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-07-06 03:06:46 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-07-06 03:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-07-06 04:03:30 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-07-06 03:03:04 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-07-06 04:02:29 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-07-06 04:01:22 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.020 |  |
| 2026-07-06 03:04:42 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.024 |  |
| 2026-07-06 04:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.084 |  |
| 2026-07-06 03:08:51 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.171 |  |
| 2026-07-06 01:07:41 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.667 |  |
| 2026-07-06 03:15:38 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -3762.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)