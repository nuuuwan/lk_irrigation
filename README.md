# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_17:19:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,733 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 17:19:34 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.031 |  |
| 2026-06-29 17:15:52 | Baddegama (Gin Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:13:47 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.080 |  |
| 2026-06-29 17:12:47 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:10:22 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.009 |  |
| 2026-06-29 17:08:17 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:08:16 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-29 17:08:00 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:07:28 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.104 |  |
| 2026-06-29 17:07:15 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:07:14 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 17:07:03 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-06-29 17:06:25 | Peradeniya (Mahaweli Ganga) | 3.03 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-06-29 17:06:22 | Panadugama (Nilwala Ganga) | 4.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 17:05:51 | Deraniyagala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.212 |  |
| 2026-06-29 17:05:49 | Ellagawa (Kalu Ganga) | 7.19 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-29 17:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.67 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-29 17:04:33 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:04:16 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 17:04:09 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-29 17:03:39 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:30 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:25 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:13 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:10 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:10 | Baddegama (Gin Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:08 | Rathnapura (Kalu Ganga) | 6.22 | 🟡 Alert | -0.035 |  |
| 2026-06-29 17:02:56 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 17:02:40 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:02:22 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-06-29 17:02:13 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:02:09 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-29 17:02:05 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:01:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:01:54 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:01:50 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-29 17:01:33 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.238 |  |
| 2026-06-29 17:01:20 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-06-29 17:01:09 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:01:04 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 17:03:08 | Rathnapura (Kalu Ganga) | 6.22 | 🟡 Alert | -0.035 |  |
| 2026-06-29 17:07:03 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-06-29 17:02:22 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-06-29 17:01:50 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-29 17:05:49 | Ellagawa (Kalu Ganga) | 7.19 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-29 17:01:20 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-06-29 17:06:25 | Peradeniya (Mahaweli Ganga) | 3.03 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-06-29 17:08:16 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-29 17:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.67 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-29 17:04:16 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 17:04:09 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-29 17:06:22 | Panadugama (Nilwala Ganga) | 4.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 17:02:56 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 17:07:14 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 17:01:54 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:01:04 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:02:13 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:01:58 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:08:17 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:02:05 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:39 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:15:52 | Baddegama (Gin Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:04:33 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:10 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:01:09 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:13 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:30 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:07:15 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:12:47 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:08:00 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:03:25 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:02:40 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 17:10:22 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.009 |  |
| 2026-06-29 17:02:09 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-29 17:19:34 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.031 |  |
| 2026-06-29 17:13:47 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.080 |  |
| 2026-06-29 17:07:28 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.104 |  |
| 2026-06-29 17:05:51 | Deraniyagala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.212 |  |
| 2026-06-29 17:01:33 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.238 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)