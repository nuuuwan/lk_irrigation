# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_14:15:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,230 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 14:15:24 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:12:25 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:12:16 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:11:26 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:11:24 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:10:41 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:10:17 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:10:14 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:09:02 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.099 |  |
| 2026-02-20 14:08:40 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-02-20 14:07:12 | Dunamale (Aththanagalu Oya) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-20 14:07:08 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-02-20 14:06:40 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.024 |  |
| 2026-02-20 14:05:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:05:33 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:05:21 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:04:40 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-02-20 14:04:31 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.030 |  |
| 2026-02-20 14:04:28 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-20 14:04:20 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:03:57 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 14:03:54 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-02-20 14:03:34 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-20 14:03:18 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:02:59 | Manampitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-02-20 14:02:58 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:02:29 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-02-20 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-02-20 14:02:08 | Padiyathalawa (Maduru Oya) | 2.18 | 🟢 Normal | -0.217 |  |
| 2026-02-20 14:01:42 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:01:38 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:01:37 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:01:37 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 14:01:31 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-20 14:01:02 | Weraganthota (Mahaweli Ganga) | -0.77 | 🟢 Normal | -0.175 |  |
| 2026-02-20 14:00:57 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-02-20 14:00:44 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 14:00:33 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-02-20 14:00:23 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 14:04:40 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-02-20 14:02:59 | Manampitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-02-20 14:03:54 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-02-20 14:03:34 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-20 14:03:57 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 14:00:44 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 14:01:37 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 14:07:12 | Dunamale (Aththanagalu Oya) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-20 14:00:11 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:01:38 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:04:20 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:03:18 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:15:24 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:11:26 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:10:17 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:10:14 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:12:25 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:05:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:02:58 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:05:33 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:01:37 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:05:21 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:12:16 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:00:23 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:01:42 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 14:08:40 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-02-20 14:04:28 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-20 14:01:31 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-20 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-02-20 14:02:29 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-02-20 14:07:08 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-02-20 14:00:33 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-02-20 14:00:57 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-02-20 14:06:40 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.024 |  |
| 2026-02-20 14:04:31 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.030 |  |
| 2026-02-20 14:09:02 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.099 |  |
| 2026-02-20 14:01:02 | Weraganthota (Mahaweli Ganga) | -0.77 | 🟢 Normal | -0.175 |  |
| 2026-02-20 14:02:08 | Padiyathalawa (Maduru Oya) | 2.18 | 🟢 Normal | -0.217 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)