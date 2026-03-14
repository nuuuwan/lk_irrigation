# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_16:10:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,260 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 16:10:24 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-14 16:09:46 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.857 | 🔺 Rising |
| 2026-03-14 16:08:11 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.047 |  |
| 2026-03-14 16:08:00 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-14 16:06:51 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 16:06:35 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-14 16:05:39 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:05:31 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:05:29 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-03-14 16:05:14 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-03-14 16:04:58 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:04:57 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:04:53 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-03-14 16:04:48 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 16:03:59 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:03:55 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 16:03:27 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-03-14 16:03:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:02:46 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.857 | 🔺 Rising |
| 2026-03-14 16:02:46 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.020 |  |
| 2026-03-14 16:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 16:02:25 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:02:21 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:02:17 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | -0.059 |  |
| 2026-03-14 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-03-14 16:02:09 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 16:02:02 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-03-14 16:01:53 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-14 16:01:45 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-14 16:01:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-14 16:01:06 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.011 |  |
| 2026-03-14 16:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:00:34 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 16:09:46 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.857 | 🔺 Rising |
| 2026-03-14 16:04:53 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-03-14 16:06:35 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-14 16:10:24 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-14 16:01:53 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-14 14:07:11 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-14 16:01:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-14 16:08:00 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-14 16:02:09 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 16:04:48 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 16:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 16:03:55 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 16:06:51 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 15:04:37 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 16:00:34 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:05:02 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:05:39 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:04:58 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:05:31 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:02:21 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:03:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:04:57 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:09:31 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:03:59 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:02:25 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:05:14 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-03-14 16:01:45 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-14 16:01:06 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.011 |  |
| 2026-03-14 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-03-14 16:02:46 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.020 |  |
| 2026-03-14 16:02:02 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-03-14 15:01:05 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-03-14 15:04:45 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-03-14 16:05:29 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-03-14 16:03:27 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-03-14 15:02:22 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.043 |  |
| 2026-03-14 16:08:11 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.047 |  |
| 2026-03-14 16:02:17 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)