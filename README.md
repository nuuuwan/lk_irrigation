# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_09:17:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,010 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 09:17:54 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.012 |  |
| 2026-01-16 09:09:25 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2026-01-16 09:08:45 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:08:18 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:08:14 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:07:53 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-16 09:07:37 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:07:15 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-16 09:06:17 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:06:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:05:37 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:05:21 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-01-16 09:05:20 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.211 |  |
| 2026-01-16 09:04:47 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:04:44 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:04:27 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:04:27 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.031 |  |
| 2026-01-16 09:03:38 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:03:28 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:03:20 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:03:11 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:03:05 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:02:52 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:02:43 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-16 09:02:29 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:02:28 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:02:07 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.035 |  |
| 2026-01-16 09:02:03 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:02:00 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:01:44 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:01:42 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:01:20 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.062 |  |
| 2026-01-16 09:01:19 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:01:16 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-01-16 09:01:12 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:01:12 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:01:09 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:00:41 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:00:40 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 09:05:21 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-01-16 09:01:16 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-01-16 09:07:15 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-16 09:02:43 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-16 09:07:53 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-16 09:01:12 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:01:42 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:00:41 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:03:05 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:03:11 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:04:27 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:04:47 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:03:38 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:02:52 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:08:45 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:05:37 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:08:18 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:06:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:06:17 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:07:37 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:02:00 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:04:44 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:01:44 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:02:28 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:08:14 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-16 09:01:12 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:03:20 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:03:28 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:00:40 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:02:29 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:01:19 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-01-16 09:17:54 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.012 |  |
| 2026-01-16 09:04:27 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.031 |  |
| 2026-01-16 09:02:07 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.035 |  |
| 2026-01-16 09:09:25 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2026-01-16 09:01:20 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.062 |  |
| 2026-01-16 09:05:20 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.211 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)