# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_00:17:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,304 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 00:17:42 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.071 |  |
| 2026-04-24 00:15:49 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-24 00:14:52 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-04-24 00:14:06 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-24 00:11:23 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-24 00:11:22 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.058 |  |
| 2026-04-24 00:11:22 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-24 00:10:29 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-24 00:07:54 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.017 |  |
| 2026-04-24 00:07:05 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 00:06:57 | Kuda Oya (Kirindi Oya) | 2.40 | 🟢 Normal | -0.046 |  |
| 2026-04-24 00:06:28 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-24 00:05:31 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.023 |  |
| 2026-04-24 00:05:27 | Thanamalwila (Kirindi Oya) | 2.35 | 🟢 Normal | -0.067 |  |
| 2026-04-24 00:05:11 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 00:04:32 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-24 00:04:28 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-24 00:04:27 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-24 00:03:47 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 00:03:46 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.342 |  |
| 2026-04-24 00:03:14 | Katharagama (Menik Ganga) | 1.13 | 🟢 Normal | 0.686 | 🔺 Rising |
| 2026-04-24 00:03:13 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-04-24 00:02:26 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-24 00:02:22 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-24 00:02:21 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 00:02:17 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2026-04-24 00:01:51 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-24 00:01:34 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-24 00:01:29 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-24 00:01:10 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-24 00:00:51 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.084 |  |
| 2026-04-24 00:00:10 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.091 |  |
| 2026-04-23 23:40:16 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.058 |  |
| 2026-04-23 23:33:01 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.017 |  |
| 2026-04-23 23:32:03 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 00:11:23 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-24 00:03:14 | Katharagama (Menik Ganga) | 1.13 | 🟢 Normal | 0.686 | 🔺 Rising |
| 2026-04-23 21:01:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-04-24 00:03:13 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-04-24 00:01:51 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-24 00:06:28 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-24 00:01:10 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-24 00:04:28 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-24 00:01:29 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-24 00:02:22 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-24 00:14:06 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-24 00:03:47 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 00:05:11 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 00:02:21 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 00:07:05 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 00:15:49 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:17:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:00:32 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 00:02:26 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-24 00:10:29 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-24 00:04:27 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-24 00:04:32 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:02:38 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-24 00:01:34 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-24 00:14:52 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-04-24 00:07:54 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.017 |  |
| 2026-04-24 00:05:31 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.023 |  |
| 2026-04-23 23:02:34 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-04-24 00:02:17 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2026-04-24 00:06:57 | Kuda Oya (Kirindi Oya) | 2.40 | 🟢 Normal | -0.046 |  |
| 2026-04-24 00:11:22 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.058 |  |
| 2026-04-24 00:05:27 | Thanamalwila (Kirindi Oya) | 2.35 | 🟢 Normal | -0.067 |  |
| 2026-04-24 00:17:42 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.071 |  |
| 2026-04-24 00:00:51 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.084 |  |
| 2026-04-24 00:00:10 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.091 |  |
| 2026-04-24 00:03:46 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.342 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)