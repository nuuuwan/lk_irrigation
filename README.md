# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_06:39:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,537 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 06:39:26 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.002 |  |
| 2026-06-08 06:15:03 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:12:49 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 1.565 | 🔺 Rising |
| 2026-06-08 06:12:26 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 1.565 | 🔺 Rising |
| 2026-06-08 06:10:38 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:10:36 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:09:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:08:54 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:08:52 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-08 06:08:30 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:07:54 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.010 |  |
| 2026-06-08 06:06:06 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.076 |  |
| 2026-06-08 06:05:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:05:22 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.071 |  |
| 2026-06-08 06:05:11 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-06-08 06:05:04 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:05:03 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-06-08 06:04:55 | Magura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.012 |  |
| 2026-06-08 06:04:34 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-06-08 06:04:22 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:03:28 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-08 06:03:28 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-08 06:03:27 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.010 |  |
| 2026-06-08 06:03:24 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-06-08 06:03:13 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:02:49 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-08 06:02:46 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.044 |  |
| 2026-06-08 06:02:42 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-08 06:02:41 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:02:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:02:17 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.058 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 06:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-06-08 06:12:49 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 1.565 | 🔺 Rising |
| 2026-06-08 06:03:28 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-08 06:02:49 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-08 06:08:52 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-08 06:02:42 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-08 06:00:18 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-08 06:39:26 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.002 |  |
| 2026-06-08 06:02:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:00:57 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:05:04 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:15:03 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:08:54 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:03:13 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:04:22 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:05:26 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:01:27 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:00:56 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:09:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:02:41 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:10:36 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:10:38 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:01:17 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:08:30 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 06:07:54 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.010 |  |
| 2026-06-08 06:03:28 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-08 06:03:27 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.010 |  |
| 2026-06-08 06:03:24 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-06-08 06:04:55 | Magura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.012 |  |
| 2026-06-08 06:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-06-08 06:05:03 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-06-08 06:05:11 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-06-08 06:04:34 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-06-08 06:02:46 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.044 |  |
| 2026-06-08 06:02:17 | Hanwella (Kelani Ganga) | 3.60 | 🟢 Normal | -0.058 |  |
| 2026-06-08 06:01:15 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | -0.062 |  |
| 2026-06-08 06:05:22 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.071 |  |
| 2026-06-08 06:06:06 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)