# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_00:37:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,885 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 00:37:17 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-03-10 00:37:16 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-03-10 00:14:23 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:10:22 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:09:01 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:08:18 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-10 00:08:02 | Moraketiya (Walawe Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:07:59 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:07:47 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:06:25 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:06:21 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 1.846 | 🔺 Rising |
| 2026-03-10 00:06:18 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:05:59 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:05:28 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:04:56 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-03-10 00:04:40 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-03-10 00:04:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:04:06 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 00:03:52 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:03:06 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 1.846 | 🔺 Rising |
| 2026-03-10 00:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:02:27 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:02:25 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:02:19 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:02:18 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.298 |  |
| 2026-03-10 00:02:10 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:01:56 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-10 00:01:48 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.030 |  |
| 2026-03-10 00:01:38 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:01:36 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:01:25 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.010 |  |
| 2026-03-10 00:01:11 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:01:08 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:00:22 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-09 23:54:53 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 00:37:17 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-03-10 00:06:21 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 1.846 | 🔺 Rising |
| 2026-03-10 00:04:40 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-03-09 18:01:06 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-10 00:01:56 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-10 00:08:18 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-09 22:02:21 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-10 00:04:06 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 00:00:22 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:05:28 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:01:36 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:01:11 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:14:23 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-03-09 18:06:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 23:10:41 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:02:25 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:06:18 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-09 23:08:10 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:01:08 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:08:02 | Moraketiya (Walawe Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:02:19 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-09 23:28:30 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:07:47 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:04:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:02:27 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:06:25 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:03:52 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:09:01 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 23:40:58 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-09 23:54:53 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:01:38 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-10 00:10:22 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-09 21:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-03-10 00:01:25 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.010 |  |
| 2026-03-10 00:01:48 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.030 |  |
| 2026-03-10 00:04:56 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.030 |  |
| 2026-03-09 18:01:53 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.075 |  |
| 2026-03-10 00:02:18 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.298 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)