# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_04:10:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,158 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 04:10:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-20 04:09:24 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:09:06 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.046 |  |
| 2026-03-20 04:06:56 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.038 |  |
| 2026-03-20 04:06:31 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:06:07 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:05:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.422 | 🔺 Rising |
| 2026-03-20 04:05:03 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 04:04:51 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-03-20 04:03:41 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:03:10 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-20 04:02:56 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:02:41 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-03-20 04:02:23 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.052 |  |
| 2026-03-20 04:02:23 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:02:20 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-20 04:02:13 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.030 |  |
| 2026-03-20 04:02:08 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-20 04:02:04 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.063 |  |
| 2026-03-20 04:02:03 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:01:59 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:01:33 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:01:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-20 04:01:24 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-03-20 04:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:01:01 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -216.000 |  |
| 2026-03-20 04:01:00 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -216.000 |  |
| 2026-03-20 04:00:59 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -216.000 |  |
| 2026-03-20 03:29:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 04:05:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.422 | 🔺 Rising |
| 2026-03-20 02:03:02 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-03-20 04:02:20 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-20 04:04:51 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-03-20 01:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-20 04:01:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-20 03:06:04 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-20 02:03:27 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-20 04:10:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-20 04:02:08 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-20 04:05:03 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 03:03:09 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 04:02:03 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:01:59 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:01:33 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:02:56 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:03:15 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:06:07 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:36:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:29:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:09:24 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:02:23 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:03:41 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:06:31 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 04:03:10 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-20 04:02:41 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-03-20 04:02:13 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.030 |  |
| 2026-03-20 04:01:24 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-03-20 04:06:56 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.038 |  |
| 2026-03-20 04:09:06 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.046 |  |
| 2026-03-20 04:02:23 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.052 |  |
| 2026-03-20 04:02:04 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.063 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-20 03:11:37 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.139 |  |
| 2026-03-20 02:20:13 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -54.000 |  |
| 2026-03-20 04:01:01 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -216.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)