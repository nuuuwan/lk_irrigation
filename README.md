# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_05:25:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,332 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 05:25:12 | Kuda Oya (Kirindi Oya) | 2.53 | 🟢 Normal | -0.193 |  |
| 2026-04-16 05:21:22 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:09:29 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-16 05:09:09 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-16 05:09:08 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:08:06 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:06:09 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-16 05:05:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:05:28 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:04:39 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-16 05:04:27 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-16 05:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-04-16 05:04:10 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.003 |  |
| 2026-04-16 05:04:06 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-16 05:03:42 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:03:39 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:03:37 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-16 05:03:27 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-04-16 05:03:11 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-04-16 05:02:45 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:02:30 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 05:02:28 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.032 |  |
| 2026-04-16 05:02:26 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-16 05:02:11 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:02:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-04-16 05:01:54 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -108.000 |  |
| 2026-04-16 05:01:52 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -108.000 |  |
| 2026-04-16 05:01:42 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-04-16 05:01:19 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.084 |  |
| 2026-04-16 05:01:10 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:01:06 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-16 05:00:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-16 05:00:25 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -108.000 |  |
| 2026-04-16 05:00:23 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -108.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 05:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-04-16 05:01:42 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-04-16 05:04:06 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-16 05:04:27 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-16 05:06:09 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-16 05:03:37 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-16 05:09:29 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-16 05:00:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-16 04:08:04 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 05:04:39 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-16 04:00:27 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-16 05:02:30 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 05:04:10 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.003 |  |
| 2026-04-16 05:05:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:21:22 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:01:19 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:02:11 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:05:28 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:03:39 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:03:42 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:08:06 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:01:10 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:09:08 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 04:01:03 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 05:09:09 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-16 05:02:26 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-16 05:03:27 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-04-16 04:03:13 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.024 |  |
| 2026-04-16 05:01:06 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-16 05:02:28 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.032 |  |
| 2026-04-16 05:02:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-16 05:03:11 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-16 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.084 |  |
| 2026-04-16 05:25:12 | Kuda Oya (Kirindi Oya) | 2.53 | 🟢 Normal | -0.193 |  |
| 2026-04-16 05:00:25 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -108.000 |  |
| 2026-04-16 05:01:54 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)