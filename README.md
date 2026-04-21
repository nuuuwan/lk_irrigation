# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_08:20:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 08:20:54 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-21 08:12:58 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:12:16 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.034 |  |
| 2026-04-21 08:11:48 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.025 |  |
| 2026-04-21 08:08:48 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.028 |  |
| 2026-04-21 08:07:31 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-21 08:06:56 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-21 08:06:34 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.085 |  |
| 2026-04-21 08:06:13 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 08:06:06 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:06:04 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-21 08:05:52 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2026-04-21 08:05:36 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-21 08:05:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.156 |  |
| 2026-04-21 08:04:55 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:04:52 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:04:29 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-04-21 08:04:23 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-21 08:04:00 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:03:57 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-21 08:03:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.048 |  |
| 2026-04-21 08:02:52 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.046 |  |
| 2026-04-21 08:02:37 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.114 |  |
| 2026-04-21 08:02:24 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-21 08:02:19 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.449 |  |
| 2026-04-21 08:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-21 08:02:14 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.59 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-21 08:02:02 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-21 08:01:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.101 |  |
| 2026-04-21 08:01:45 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:01:25 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.065 |  |
| 2026-04-21 08:01:15 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.041 |  |
| 2026-04-21 08:01:07 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 08:01:00 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:00:59 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.043 |  |
| 2026-04-21 08:00:33 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.134 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 08:03:57 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-21 08:06:13 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 08:02:02 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-21 08:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.59 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-21 08:04:23 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-21 08:06:56 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-21 08:06:04 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-21 08:20:54 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-21 08:01:07 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 07:11:05 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-21 08:12:58 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:02:14 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:01:45 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:04:52 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:04:55 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:04:00 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:01:00 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:06:06 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-21 08:07:31 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-21 08:02:24 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-21 08:05:36 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-21 08:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-21 08:11:48 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.025 |  |
| 2026-04-21 08:08:48 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.028 |  |
| 2026-04-21 08:05:52 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2026-04-21 08:04:29 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-04-21 08:12:16 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.034 |  |
| 2026-04-21 08:01:15 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.041 |  |
| 2026-04-21 08:00:59 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.043 |  |
| 2026-04-21 08:02:52 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.046 |  |
| 2026-04-21 08:03:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.048 |  |
| 2026-04-21 08:01:25 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.065 |  |
| 2026-04-21 08:06:34 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.085 |  |
| 2026-04-21 07:26:21 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.091 |  |
| 2026-04-21 08:01:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.101 |  |
| 2026-04-21 08:02:37 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.114 |  |
| 2026-04-21 08:00:33 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.134 |  |
| 2026-04-21 08:05:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.156 |  |
| 2026-04-21 08:02:19 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.449 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)