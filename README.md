# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_09:10:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,580 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 09:10:56 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.101 |  |
| 2026-05-30 09:09:25 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:08:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-30 09:08:25 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.080 |  |
| 2026-05-30 09:07:38 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:07:23 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:06:35 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-05-30 09:06:31 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:06:27 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:05:44 | Rathnapura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.078 |  |
| 2026-05-30 09:05:42 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-05-30 09:05:22 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.023 |  |
| 2026-05-30 09:05:10 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.354 |  |
| 2026-05-30 09:04:11 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 09:03:57 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:03:57 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.011 |  |
| 2026-05-30 09:03:56 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:03:44 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:03:42 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:03:17 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:03:01 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-05-30 09:02:50 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:02:48 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 09:02:37 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.052 |  |
| 2026-05-30 09:02:36 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-30 09:02:27 | Ellagawa (Kalu Ganga) | 7.95 | 🟢 Normal | -0.070 |  |
| 2026-05-30 09:02:23 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:02:22 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:02:19 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | -0.020 |  |
| 2026-05-30 09:02:19 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:02:11 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.032 |  |
| 2026-05-30 09:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.49 | 🟡 Alert | -0.032 |  |
| 2026-05-30 09:02:02 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:01:41 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | -0.032 |  |
| 2026-05-30 09:01:29 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:01:23 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 09:01:11 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:01:06 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:00:45 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.050 |  |
| 2026-05-30 09:00:43 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 08:30:23 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 09:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.49 | 🟡 Alert | -0.032 |  |
| 2026-05-30 09:02:36 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-30 09:08:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-30 09:01:23 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 09:02:48 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 09:04:11 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 09:03:57 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:00:43 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:02:19 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:01:29 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:03:17 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:02:23 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:06:27 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:03:42 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:02:50 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:03:56 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:01:06 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:07:23 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:07:38 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:02:02 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:09:25 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:01:11 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:02:22 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:05:42 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-05-30 09:06:35 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-05-30 09:03:01 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-05-30 09:03:57 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.011 |  |
| 2026-05-30 09:02:19 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | -0.020 |  |
| 2026-05-30 09:05:22 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.023 |  |
| 2026-05-30 09:01:41 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | -0.032 |  |
| 2026-05-30 09:02:11 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.032 |  |
| 2026-05-30 09:00:45 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.050 |  |
| 2026-05-30 09:02:37 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.052 |  |
| 2026-05-30 09:02:27 | Ellagawa (Kalu Ganga) | 7.95 | 🟢 Normal | -0.070 |  |
| 2026-05-30 09:05:44 | Rathnapura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.078 |  |
| 2026-05-30 09:08:25 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.080 |  |
| 2026-05-30 09:10:56 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.101 |  |
| 2026-05-30 09:05:10 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.354 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)