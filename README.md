# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_21:25:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,074 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 21:25:06 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:20:45 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.062 |  |
| 2026-03-06 21:11:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:07:58 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-03-06 21:06:14 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:06:12 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:05:39 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:05:22 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-06 21:04:52 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-03-06 21:04:50 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.095 |  |
| 2026-03-06 21:04:45 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-03-06 21:04:39 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.050 |  |
| 2026-03-06 21:04:20 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:04:07 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-03-06 21:04:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:03:55 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:03:46 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-06 21:03:45 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-03-06 21:03:40 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:03:29 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:03:09 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:48 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:43 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:35 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:31 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:17 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:12 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-06 21:01:58 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:01:54 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:01:42 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:01:17 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 21:01:16 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:01:13 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 20:43:30 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 20:36:36 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 20:34:47 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 21:07:58 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-03-06 21:05:22 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-06 21:03:46 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-06 21:02:12 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-06 21:01:17 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 21:01:54 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:03:09 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:01:42 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:03:40 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:01:13 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:48 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:17 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-06 18:01:33 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:31 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:05:39 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 20:16:16 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:04:20 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:03:55 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:43 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:01:58 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:04:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:03:29 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:02:35 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:06:14 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:01:16 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 18:03:37 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:25:06 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:06:12 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:11:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:04:52 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-03-06 21:04:45 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-03-06 21:04:07 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-03-06 21:03:45 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-03-06 21:04:39 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.050 |  |
| 2026-03-06 18:03:18 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.051 |  |
| 2026-03-06 21:20:45 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.062 |  |
| 2026-03-06 21:04:50 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.095 |  |
| 2026-03-06 20:10:51 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.228 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)