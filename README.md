# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_07:32:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 07:32:22 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-07 07:27:34 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-07 07:13:18 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 07:10:17 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-07 07:09:28 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:09:03 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:08:11 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.064 |  |
| 2026-06-07 07:07:49 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-07 07:07:36 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-07 07:07:29 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | 0.511 | 🔺 Rising |
| 2026-06-07 07:07:28 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.005 |  |
| 2026-06-07 07:07:19 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 07:06:03 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 07:06:03 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-06-07 07:05:59 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.018 |  |
| 2026-06-07 07:04:38 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-07 07:03:47 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-07 07:03:44 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-06-07 07:03:41 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:03:37 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-06-07 07:03:24 | Deraniyagala (Kelani Ganga) | 2.63 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-07 07:03:16 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 07:03:07 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-07 07:03:07 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-06-07 07:02:50 | Nawalapitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.258 |  |
| 2026-06-07 07:02:45 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-07 07:02:40 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:02:22 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-07 07:02:18 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:02:11 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.002 |  |
| 2026-06-07 07:02:05 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:01:37 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-06-07 07:01:31 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:01:16 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.071 |  |
| 2026-06-07 07:01:08 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:00:41 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:00:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 07:07:29 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | 0.511 | 🔺 Rising |
| 2026-06-07 06:07:18 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-06-07 07:03:07 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-06-07 07:03:44 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-06-07 07:07:36 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-07 07:04:38 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-07 07:02:22 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-07 07:07:49 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-07 07:03:07 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-07 07:03:24 | Deraniyagala (Kelani Ganga) | 2.63 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-07 07:27:34 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-07 07:03:47 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-07 07:02:45 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-07 07:10:17 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-07 06:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 07:03:16 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 07:07:19 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 07:06:03 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 07:13:18 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 07:32:22 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-07 07:07:28 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.005 |  |
| 2026-06-07 07:02:11 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.002 |  |
| 2026-06-07 07:01:08 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:02:05 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:00:41 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:03:41 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:09:03 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:00:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:02:18 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:09:28 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:01:31 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:02:40 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 07:03:37 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-06-07 07:05:59 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.018 |  |
| 2026-06-07 07:06:03 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-06-07 07:01:37 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-06-07 07:08:11 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.064 |  |
| 2026-06-07 07:01:16 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.071 |  |
| 2026-06-07 07:02:50 | Nawalapitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.258 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)