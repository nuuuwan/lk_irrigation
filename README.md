# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--27_18:13:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **57,248 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 18:13:16 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:09:28 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:06:53 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:06:03 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:05:00 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:04:58 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:04:57 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-01-27 18:04:41 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:03:59 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:03:56 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-01-27 18:03:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:03:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-27 18:03:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:03:26 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:03:19 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-27 18:02:53 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-27 18:02:47 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-01-27 18:02:44 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-01-27 18:02:29 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:02:25 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-27 18:02:25 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 18:02:23 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:02:11 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-01-27 18:01:58 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:01:53 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:01:49 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-01-27 18:01:49 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.021 |  |
| 2026-01-27 18:01:45 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:01:40 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 18:01:40 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:01:39 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-27 18:01:29 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-01-27 18:01:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 18:01:22 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.031 |  |
| 2026-01-27 18:00:55 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-27 18:00:40 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:00:40 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 17:43:04 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-27 17:33:06 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 18:00:55 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-27 18:03:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-27 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-27 18:01:40 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 18:01:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 18:02:25 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 18:00:40 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:03:59 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:01:53 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:01:39 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:01:45 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:02:11 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:04:41 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:02:29 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:09:28 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:06:53 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:02:23 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-27 17:08:40 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:03:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:05:00 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:13:16 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:01:58 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 17:04:13 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-27 17:04:19 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:01:40 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:06:03 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-27 18:03:19 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-27 18:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-01-27 18:02:25 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-27 17:06:09 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-27 18:01:29 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-01-27 18:04:57 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-01-27 18:03:56 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-01-27 18:02:47 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-01-27 18:02:53 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-27 18:01:49 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.021 |  |
| 2026-01-27 18:02:44 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-01-27 18:01:49 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-01-27 18:01:22 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)