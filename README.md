# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--27_12:00:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **108,705 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 12:00:25 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:18:51 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | -0.008 |  |
| 2026-03-27 11:16:00 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.026 |  |
| 2026-03-27 11:11:55 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:10:04 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:08:51 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-03-27 11:08:48 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.145 |  |
| 2026-03-27 11:07:43 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:06:56 | Ellagawa (Kalu Ganga) | 3.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:06:49 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-03-27 11:06:39 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 11:06:49 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-03-27 11:03:27 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-27 11:03:06 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-27 11:02:59 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 11:02:05 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-27 12:00:25 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:06:13 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:02:54 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:01:17 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:04:38 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:02:38 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:11:55 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:01:36 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:01:18 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:02:45 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:06:56 | Ellagawa (Kalu Ganga) | 3.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 10:03:57 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:04:17 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:00:22 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:01:32 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:06:39 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:07:43 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:06:26 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:10:04 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:01:40 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-27 11:18:51 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | -0.008 |  |
| 2026-03-27 11:05:29 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-27 11:00:54 | Horowpothana (Yan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-27 11:05:05 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-03-27 11:08:51 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-03-27 11:16:00 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.026 |  |
| 2026-03-27 11:06:29 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-03-27 11:03:43 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.031 |  |
| 2026-03-27 11:01:34 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-03-27 11:04:39 | Panadugama (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.034 |  |
| 2026-03-27 11:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.039 |  |
| 2026-03-27 11:01:36 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.049 |  |
| 2026-03-27 11:08:48 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.145 |  |
| 2026-03-27 11:01:21 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.184 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)