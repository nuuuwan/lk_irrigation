# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_22:19:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,816 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 22:19:31 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-02 22:16:51 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:16:45 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-02 22:14:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:12:22 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:10:54 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.019 |  |
| 2026-02-02 22:10:12 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:06:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:05:43 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:05:32 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-02 22:05:06 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-02 22:04:48 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.029 |  |
| 2026-02-02 22:04:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:04:30 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 22:03:50 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:03:37 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-02 22:03:33 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:03:25 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:03:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:03:00 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 22:02:59 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:02:58 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:02:32 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.128 |  |
| 2026-02-02 22:02:21 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-02-02 22:02:19 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:02:17 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-02-02 22:01:59 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 22:01:56 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-02-02 22:01:30 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:01:25 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:01:08 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 22:00:55 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-02 22:00:44 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:00:33 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:00:20 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:00:15 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 22:02:21 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-02-02 22:01:56 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-02-02 22:03:37 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-02 22:05:06 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-02 22:05:32 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-02 22:01:59 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 22:16:45 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-02 22:19:31 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-02 22:04:30 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 22:01:08 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 22:03:00 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 22:01:30 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:04:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:02:59 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:00:44 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:09:57 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:10:12 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:12:22 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:16:51 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:00:33 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:14:29 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:03:33 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:05:43 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:00:20 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:00:15 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:06:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:03:50 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:02:58 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:01:25 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:03:25 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:02:19 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-02 21:08:43 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.018 |  |
| 2026-02-02 22:10:54 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.019 |  |
| 2026-02-02 22:00:55 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-02 22:04:48 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.029 |  |
| 2026-02-02 22:02:17 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-02-02 18:01:17 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.061 |  |
| 2026-02-02 22:02:32 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)