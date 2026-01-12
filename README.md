# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_08:16:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,403 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 08:16:15 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:11:49 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -1.241 |  |
| 2026-01-12 08:11:20 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -1.241 |  |
| 2026-01-12 08:11:06 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:10:44 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-01-12 08:09:23 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:08:37 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-01-12 08:07:43 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.035 |  |
| 2026-01-12 08:07:42 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-01-12 08:07:30 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:07:22 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-01-12 08:07:03 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-01-12 08:06:54 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-01-12 08:06:29 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:06:10 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:06:09 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-01-12 08:05:54 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:05:48 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:05:43 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-01-12 08:05:18 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-12 08:05:11 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.048 |  |
| 2026-01-12 08:05:10 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-12 08:04:30 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-01-12 08:04:03 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:03:18 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 08:02:58 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 08:02:42 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:02:41 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-12 08:02:20 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:02:16 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 08:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.050 |  |
| 2026-01-12 08:01:50 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-01-12 08:01:49 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-12 08:01:48 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-12 08:01:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:01:22 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:01:21 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:01:00 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | -0.011 |  |
| 2026-01-12 07:29:33 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:24:15 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:19:49 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 08:07:42 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-01-12 08:05:18 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-12 08:01:48 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-12 08:02:58 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 08:02:16 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 08:05:10 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-12 08:03:18 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 08:01:22 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:02:42 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:07:30 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:16:15 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:01:21 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:11:06 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:04:03 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:05:48 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:06:10 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:01:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:05:54 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:06:29 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:09:23 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:12:23 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:05:29 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:02:20 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 08:10:44 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-01-12 08:05:43 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-01-12 08:08:37 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-01-12 08:02:41 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-12 08:06:54 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-01-12 08:01:49 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-12 08:01:00 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | -0.011 |  |
| 2026-01-12 08:06:09 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-01-12 08:04:30 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-01-12 08:01:50 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-01-12 08:07:03 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-01-12 08:07:43 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.035 |  |
| 2026-01-12 08:05:11 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.048 |  |
| 2026-01-12 08:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.050 |  |
| 2026-01-12 07:08:19 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.170 |  |
| 2026-01-12 08:11:49 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -1.241 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)