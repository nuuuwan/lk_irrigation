# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_05:19:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,196 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 05:19:11 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.017 |  |
| 2026-03-20 05:13:57 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:10:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.152 |  |
| 2026-03-20 05:10:05 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.046 |  |
| 2026-03-20 05:09:28 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:09:06 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.209 |  |
| 2026-03-20 05:08:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:07:50 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:06:38 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 05:06:04 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 05:05:56 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-03-20 05:05:47 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.038 |  |
| 2026-03-20 05:05:44 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.331 | 🔺 Rising |
| 2026-03-20 05:05:36 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-03-20 05:05:25 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-03-20 05:05:00 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-03-20 05:04:49 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.005 |  |
| 2026-03-20 05:03:38 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:03:35 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:03:21 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-03-20 05:03:12 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:02:45 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -1.241 |  |
| 2026-03-20 05:02:43 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:02:27 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-03-20 05:02:21 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:01:58 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:01:55 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 05:01:47 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -1.241 |  |
| 2026-03-20 05:01:43 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-03-20 05:01:06 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:00:46 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-20 05:00:25 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:51:23 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:33:11 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | 0.805 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 04:33:11 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | 0.805 | 🔺 Rising |
| 2026-03-20 04:05:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.422 | 🔺 Rising |
| 2026-03-20 05:05:44 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.331 | 🔺 Rising |
| 2026-03-20 05:01:43 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-03-20 02:03:02 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-03-20 05:00:46 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-20 01:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-20 04:01:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-20 05:01:55 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 05:06:04 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 05:06:38 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 05:04:49 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.005 |  |
| 2026-03-20 05:09:28 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:01:58 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:02:43 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:01:06 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:00:25 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:13:57 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:03:35 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:02:21 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:03:38 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:07:50 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:08:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-20 05:05:25 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-03-20 05:05:36 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-03-20 05:05:00 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-03-20 05:19:11 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.017 |  |
| 2026-03-20 05:05:56 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-03-20 05:03:21 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-03-20 05:02:27 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-03-20 05:05:47 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.038 |  |
| 2026-03-20 04:06:56 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.038 |  |
| 2026-03-20 05:10:05 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.046 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-20 05:10:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.152 |  |
| 2026-03-20 05:09:06 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.209 |  |
| 2026-03-20 05:02:45 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -1.241 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)