# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_19:12:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,320 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 19:12:05 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-02-21 19:09:23 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-02-21 19:08:04 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:07:57 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.387 | 🔺 Rising |
| 2026-02-21 19:07:50 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-21 19:07:24 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-21 19:07:19 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.072 |  |
| 2026-02-21 19:07:16 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | 1.509 | 🔺 Rising |
| 2026-02-21 19:05:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-21 19:05:56 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-21 19:05:47 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 19:05:43 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 19:05:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.122 |  |
| 2026-02-21 19:04:55 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-02-21 19:04:39 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:04:23 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-02-21 19:04:17 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-21 19:04:16 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 1.039 | 🔺 Rising |
| 2026-02-21 19:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-02-21 19:03:16 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-02-21 19:02:56 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 19:02:38 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:02:38 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:02:29 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:02:21 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:02:20 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-21 19:02:14 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-21 19:02:13 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-21 19:02:09 | Nakkala (Kumbukkan Oya) | 4.95 | 🟢 Normal | 2.056 | 🔺 Rising |
| 2026-02-21 19:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-02-21 19:00:21 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.102 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 19:02:09 | Nakkala (Kumbukkan Oya) | 4.95 | 🟢 Normal | 2.056 | 🔺 Rising |
| 2026-02-21 19:07:16 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | 1.509 | 🔺 Rising |
| 2026-02-21 19:04:16 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 1.039 | 🔺 Rising |
| 2026-02-21 18:06:43 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-02-21 19:03:16 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-02-21 19:07:57 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.387 | 🔺 Rising |
| 2026-02-21 19:04:55 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-02-21 18:08:11 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-02-21 19:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-02-21 19:12:05 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-02-21 19:07:24 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-21 19:05:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-21 19:04:17 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-21 19:05:56 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-21 19:07:50 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-21 19:02:14 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-21 17:53:34 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-21 19:05:47 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 19:02:20 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-21 19:02:56 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 19:05:43 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 19:02:29 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:01:16 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:04:39 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:02:38 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:02:21 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:08:04 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:08 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:02:38 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 19:04:23 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-02-21 19:09:23 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-02-21 19:02:13 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-21 19:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-21 19:07:19 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.072 |  |
| 2026-02-21 19:00:21 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.102 |  |
| 2026-02-21 19:05:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)