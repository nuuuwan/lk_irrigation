# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_20:42:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 20:42:41 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:14:17 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:11:39 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.031 |  |
| 2026-02-16 20:08:44 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.009 |  |
| 2026-02-16 20:08:27 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:07:53 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-16 20:07:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.049 |  |
| 2026-02-16 20:06:59 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:06:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-02-16 20:06:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:05:51 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:05:35 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:05:14 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-02-16 20:04:34 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:04:32 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:04:30 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:04:06 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.486 |  |
| 2026-02-16 20:03:31 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:03:28 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-16 20:03:25 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-02-16 20:03:23 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.030 |  |
| 2026-02-16 20:03:03 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:03:02 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:02:38 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-16 20:02:28 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:02:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:02:07 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-16 20:01:58 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:01:54 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 20:01:49 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.043 |  |
| 2026-02-16 20:01:42 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:01:32 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-16 20:01:24 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:01:21 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:01:01 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.012 |  |
| 2026-02-16 20:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 20:02:38 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-16 20:03:28 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-16 20:02:07 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-16 20:07:53 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-16 20:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 20:01:54 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 20:06:59 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:01:21 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:01:58 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:01:42 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:03:31 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:03:59 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:02:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:04:30 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:14:17 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:42:41 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:04:34 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:05:51 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:01:24 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:04:32 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:03:02 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:05:35 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:06:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 18:01:36 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:08:27 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:02:28 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-16 20:08:44 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.009 |  |
| 2026-02-16 20:05:14 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-02-16 20:01:32 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-16 20:03:25 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-02-16 20:01:01 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.012 |  |
| 2026-02-16 19:03:43 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-02-16 20:03:23 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.030 |  |
| 2026-02-16 20:11:39 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.031 |  |
| 2026-02-16 20:06:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-02-16 20:01:49 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.043 |  |
| 2026-02-16 20:07:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.049 |  |
| 2026-02-16 18:00:50 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.131 |  |
| 2026-02-16 20:04:06 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.486 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)