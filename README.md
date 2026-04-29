# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_03:36:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,741 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 03:36:09 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-30 03:34:06 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.013 |  |
| 2026-04-30 03:28:08 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-30 03:23:01 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-30 03:08:25 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-30 03:07:56 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:07:54 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -181.636 |  |
| 2026-04-30 03:07:51 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:07:45 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -1.636 |  |
| 2026-04-30 03:07:39 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-04-30 03:07:32 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -181.636 |  |
| 2026-04-30 03:07:23 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -1.636 |  |
| 2026-04-30 03:06:27 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:04:09 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-04-30 03:04:07 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.049 |  |
| 2026-04-30 03:04:02 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:03:54 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:03:40 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-30 03:03:31 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.134 |  |
| 2026-04-30 03:03:25 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-30 03:03:21 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-30 03:03:00 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.057 |  |
| 2026-04-30 03:02:54 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:02:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.092 |  |
| 2026-04-30 03:02:12 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-30 03:02:11 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:01:50 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-30 03:01:42 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:01:28 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:01:17 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:01:09 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.040 |  |
| 2026-04-30 03:00:56 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 03:04:09 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-04-30 03:03:40 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-30 03:02:12 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-30 03:03:21 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-30 03:03:25 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-30 02:18:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-30 03:01:50 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 03:23:01 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-30 03:36:09 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 03:28:08 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-30 03:00:56 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:03:11 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:04:02 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:02:11 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:28:10 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:02:54 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:07:51 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:06:27 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:01:17 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:01:42 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:07:56 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:02:28 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:01:28 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 03:07:39 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-04-30 01:03:44 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-30 03:08:25 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-30 03:34:06 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.013 |  |
| 2026-04-30 03:01:09 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.040 |  |
| 2026-04-30 03:04:07 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.049 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-30 03:03:00 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.057 |  |
| 2026-04-30 01:07:52 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-04-30 03:02:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.092 |  |
| 2026-04-30 03:03:31 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.134 |  |
| 2026-04-30 03:07:45 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -1.636 |  |
| 2026-04-30 03:07:54 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -181.636 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)