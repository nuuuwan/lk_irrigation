# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_23:16:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,086 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 23:16:52 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:16:29 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:14:07 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:13:58 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 23:11:50 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.085 |  |
| 2026-01-11 23:09:12 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-01-11 23:06:01 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 23:05:50 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-01-11 23:05:41 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-01-11 23:05:33 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.500 | 🔺 Rising |
| 2026-01-11 23:05:24 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:04:55 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 23:04:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 23:04:38 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 23:04:37 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-11 23:03:35 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 23:03:32 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:29 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:25 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:25 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-11 23:03:16 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:05 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 23:02:42 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 23:01:34 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.062 |  |
| 2026-01-11 23:01:33 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:01:30 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 23:01:26 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:01:11 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-11 23:01:08 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-01-11 23:01:05 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 23:00:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 23:00:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 23:00:08 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 22:20:03 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 23:05:33 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.500 | 🔺 Rising |
| 2026-01-11 23:09:12 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-01-11 23:03:25 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-11 23:04:37 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-11 23:04:38 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 22:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 23:03:05 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 23:03:35 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 23:06:01 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 23:04:55 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 23:01:11 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-11 23:13:58 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 23:00:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 23:00:08 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 23:00:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 22:02:30 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 23:01:30 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 23:02:42 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:16:52 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:01:26 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:20:51 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:25 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:01:33 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:29 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:05:24 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:32 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:14:07 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-11 22:05:33 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:16 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:05:41 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-01-11 23:05:50 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-01-11 23:01:05 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 23:04:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 23:01:08 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-01-11 23:01:34 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.062 |  |
| 2026-01-11 23:11:50 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)