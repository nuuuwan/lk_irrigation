# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_15:13:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,034 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 15:13:21 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-04 15:10:19 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:08:39 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.044 |  |
| 2026-04-04 15:07:29 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-04 15:06:23 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.056 |  |
| 2026-04-04 15:06:21 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-04 15:06:16 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:05:55 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:05:50 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 15:05:32 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-04 15:05:31 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 15:05:27 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:04:46 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.019 |  |
| 2026-04-04 15:04:43 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 15:04:40 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-04 15:04:38 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-04 15:04:16 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.191 |  |
| 2026-04-04 15:03:56 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-04 15:03:48 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:03:48 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:03:18 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-04 15:03:13 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 15:03:06 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:02:35 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-04-04 15:02:35 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-04 15:02:28 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:02:24 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-04 15:02:15 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-04-04 15:02:01 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-04-04 15:01:57 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-04 15:01:48 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:01:29 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:01:24 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:01:22 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:01:19 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:01:03 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:01:02 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -24.000 |  |
| 2026-04-04 15:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 15:00:45 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.021 |  |
| 2026-04-04 15:00:41 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -24.000 |  |
| 2026-04-04 15:00:13 | Thanthirimale (Malwathu Oya) | 2.60 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 15:02:35 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-04-04 15:13:21 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-04 15:04:40 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-04 15:07:29 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-04 15:03:18 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-04 15:05:32 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-04 15:04:43 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 15:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 15:03:13 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 15:05:31 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 15:05:50 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 15:01:48 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:01:22 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:06:16 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:01:24 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:01:19 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:01:29 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:03:06 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:05:27 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:03:48 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:03:48 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:02:15 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:05:55 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:02:28 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:10:19 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 15:02:35 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-04 15:00:13 | Thanthirimale (Malwathu Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-04-04 15:02:24 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-04 15:06:21 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-04 15:02:01 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-04-04 15:04:46 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.019 |  |
| 2026-04-04 15:04:38 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-04 15:03:56 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-04 15:00:45 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.021 |  |
| 2026-04-04 15:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-04-04 15:08:39 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.044 |  |
| 2026-04-04 15:06:23 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.056 |  |
| 2026-04-04 15:04:16 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.191 |  |
| 2026-04-04 15:01:02 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -24.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)