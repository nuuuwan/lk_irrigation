# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_12:06:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,427 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 12:06:39 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:06:28 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:05:39 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.029 |  |
| 2026-03-09 12:05:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:03:58 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:03:57 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 12:03:51 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.214 |  |
| 2026-03-09 12:03:26 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 12:03:25 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-09 12:03:10 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:03:07 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:02:58 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.098 |  |
| 2026-03-09 12:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-03-09 12:02:41 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-09 12:02:37 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.059 |  |
| 2026-03-09 12:02:36 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:02:24 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.073 |  |
| 2026-03-09 12:02:18 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:02:06 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 12:02:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:01:59 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:01:49 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:01:44 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:01:42 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 12:01:41 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:01:31 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-03-09 12:01:30 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 12:01:30 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-03-09 12:00:54 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 12:00:43 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-09 12:00:10 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.073 |  |
| 2026-03-09 12:00:10 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:42:58 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-03-09 11:27:53 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:20:17 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:19:59 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-03-09 11:16:47 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 12:01:30 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-03-09 12:03:25 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-09 12:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 12:03:26 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 12:00:54 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 12:01:30 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 12:01:42 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 12:03:57 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 12:01:59 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:02:18 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:00:10 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:01:49 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:03:07 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:03:10 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:06:39 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:01:08 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:07:10 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:02:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:01:44 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:06:28 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:02:36 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:01:41 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:05:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:02:06 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:03:58 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 11:19:59 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-03-09 11:07:27 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-03-09 12:00:43 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-09 12:02:41 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-09 11:10:38 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-09 12:01:31 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-03-09 11:03:06 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.019 |  |
| 2026-03-09 12:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-03-09 12:05:39 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.029 |  |
| 2026-03-09 12:02:37 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.059 |  |
| 2026-03-09 12:00:10 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.073 |  |
| 2026-03-09 12:02:24 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.073 |  |
| 2026-03-09 12:02:58 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.098 |  |
| 2026-03-09 12:03:51 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)