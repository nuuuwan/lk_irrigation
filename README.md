# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_06:15:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 06:15:44 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.025 |  |
| 2026-02-25 06:14:39 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.034 |  |
| 2026-02-25 06:14:15 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:12:02 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.013 |  |
| 2026-02-25 06:11:03 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:08:59 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.046 |  |
| 2026-02-25 06:08:50 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:08:18 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-25 06:05:56 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.006 |  |
| 2026-02-25 06:05:53 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:05:52 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-25 06:05:40 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:05:34 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:05:09 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:04:41 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-25 06:04:34 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-25 06:04:18 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:04:13 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:03:46 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -72.000 |  |
| 2026-02-25 06:03:45 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -72.000 |  |
| 2026-02-25 06:03:37 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-25 06:03:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.054 |  |
| 2026-02-25 06:03:22 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:02:59 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.068 |  |
| 2026-02-25 06:02:57 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-02-25 06:02:49 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:02:41 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:02:24 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:02:22 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.022 |  |
| 2026-02-25 06:01:50 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:01:49 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:01:47 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:01:46 | Pitabeddara (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.359 |  |
| 2026-02-25 06:01:44 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:01:35 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:01:34 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-25 06:00:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:00:37 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:00:31 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-02-25 06:00:26 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-02-25 05:53:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.359 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 06:08:18 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-25 06:03:37 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-25 06:05:52 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-25 06:02:41 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:05:34 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:03:22 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:02:24 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:11:03 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-25 05:01:32 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:00:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:05:09 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:02:49 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:00:37 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:05:53 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:04:13 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:14:15 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:04:18 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:05:40 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:08:50 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:01:35 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:01:44 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 06:05:56 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.006 |  |
| 2026-02-25 06:04:34 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-25 06:04:41 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-25 06:01:34 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-25 06:00:26 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-02-25 06:02:57 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-02-25 06:12:02 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.013 |  |
| 2026-02-25 06:00:31 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-02-25 06:02:22 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.022 |  |
| 2026-02-25 06:15:44 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.025 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-25 06:14:39 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.034 |  |
| 2026-02-25 06:08:59 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.046 |  |
| 2026-02-25 06:03:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.054 |  |
| 2026-02-25 06:02:59 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.068 |  |
| 2026-02-25 06:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.359 |  |
| 2026-02-25 06:03:46 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)