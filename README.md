# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_04:47:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,955 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 04:47:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 5.268 | 🔺 Rising |
| 2026-06-22 04:46:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 5.268 | 🔺 Rising |
| 2026-06-22 04:41:15 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.046 |  |
| 2026-06-22 04:34:13 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.004 |  |
| 2026-06-22 04:15:22 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.046 |  |
| 2026-06-22 04:14:53 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-22 04:11:49 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:11:14 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:10:21 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-06-22 04:10:06 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-22 04:09:16 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.138 |  |
| 2026-06-22 04:07:36 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-06-22 04:07:24 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 04:47:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 5.268 | 🔺 Rising |
| 2026-06-22 04:07:36 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-06-22 04:14:53 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-22 04:06:31 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-22 04:04:01 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-22 04:01:35 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-22 04:02:44 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 04:03:56 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 04:01:19 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:01:27 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:02:01 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:03:46 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:01:27 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:11:14 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:07:24 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:16 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:01:24 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:06:26 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:04:05 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:05:09 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:01:32 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:11:49 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 04:34:13 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.004 |  |
| 2026-06-22 04:10:21 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-06-22 04:10:06 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-22 04:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-21 21:01:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-22 04:02:40 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-06-22 04:01:08 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-22 04:02:41 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-22 04:05:12 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | -0.020 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-22 04:01:25 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.021 |  |
| 2026-06-22 04:05:31 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.025 |  |
| 2026-06-22 04:41:15 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.046 |  |
| 2026-06-22 04:09:16 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.138 |  |
| 2026-06-22 04:02:20 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.349 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)