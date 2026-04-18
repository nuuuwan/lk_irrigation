# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_16:13:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,547 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 16:13:30 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:11:59 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:10:50 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:09:30 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:09:25 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -24.000 |  |
| 2026-04-18 16:09:22 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -24.000 |  |
| 2026-04-18 16:08:10 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-18 16:07:42 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:07:22 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.488 | 🔺 Rising |
| 2026-04-18 16:07:18 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-18 16:06:33 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 16:06:22 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-18 16:04:48 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-04-18 16:04:44 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-04-18 16:04:25 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-04-18 16:04:08 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:04:01 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:54 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:54 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:52 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:23 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:19 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:08 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:06 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-04-18 16:03:03 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 16:02:59 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-04-18 16:02:58 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-18 16:02:45 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-04-18 16:02:44 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:02:43 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:02:20 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:02:07 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:01:42 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:01:31 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:01:27 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:01:08 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-18 16:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:01:07 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-04-18 16:00:51 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:00:33 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:00:17 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.031 |  |
| 2026-04-18 16:00:08 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 16:07:22 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.488 | 🔺 Rising |
| 2026-04-18 16:03:06 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-04-18 16:06:33 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 16:06:22 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-18 16:02:58 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-18 16:03:03 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 16:02:44 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:00:08 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:01:31 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:01:27 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:00:33 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:08 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:04:08 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:54 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:04:01 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:23 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:01:42 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:09:30 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:10:50 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:54 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:02:20 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:07:42 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:19 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:00:51 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:11:59 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:13:30 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:01:08 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-18 16:07:18 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-18 16:01:07 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-04-18 16:04:25 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-04-18 16:08:10 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-18 16:04:44 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-04-18 16:02:59 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-04-18 16:04:48 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-04-18 16:00:17 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.031 |  |
| 2026-04-18 16:02:45 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-04-18 16:09:25 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -24.000 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)