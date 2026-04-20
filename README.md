# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_06:38:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,917 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 06:38:55 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-20 06:18:54 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:18:52 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:08:45 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-20 06:08:39 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:08:09 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -5.400 |  |
| 2026-04-20 06:07:49 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -5.400 |  |
| 2026-04-20 06:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.057 |  |
| 2026-04-20 06:06:05 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 06:05:51 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 06:05:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-04-20 06:05:39 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.014 |  |
| 2026-04-20 06:05:01 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:04:42 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:04:36 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.075 |  |
| 2026-04-20 06:04:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 06:03:44 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:03:44 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.023 |  |
| 2026-04-20 06:03:29 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:03:22 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:03:07 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:02:51 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-20 06:02:43 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-20 06:02:41 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 06:02:31 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 06:02:14 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-04-20 06:02:02 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:01:25 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.120 |  |
| 2026-04-20 06:01:20 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-04-20 06:01:09 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 06:01:08 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-20 06:00:53 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-04-20 06:00:51 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 06:00:43 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:00:39 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.041 |  |
| 2026-04-20 06:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.023 |  |
| 2026-04-20 06:00:25 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-20 06:00:12 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 06:01:20 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-04-20 06:02:14 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-04-20 06:00:53 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-04-20 06:08:45 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-20 06:01:08 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-20 06:00:25 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-20 06:02:43 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-20 06:02:51 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-20 05:33:41 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-20 06:02:31 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 06:01:09 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 06:02:41 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 06:05:51 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 06:00:51 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 06:04:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 06:06:05 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 06:38:55 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-20 06:00:12 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:00:43 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:02:02 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:03:44 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:18:54 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:03:29 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:04:42 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:08:39 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:03:07 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:03:22 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:05:01 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-20 06:05:39 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.014 |  |
| 2026-04-20 06:03:44 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.023 |  |
| 2026-04-20 06:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.023 |  |
| 2026-04-20 06:05:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.033 |  |
| 2026-04-20 06:00:39 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.041 |  |
| 2026-04-20 06:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.057 |  |
| 2026-04-20 06:04:36 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.075 |  |
| 2026-04-20 05:23:02 | Kithulgala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.081 |  |
| 2026-04-20 06:01:25 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.120 |  |
| 2026-04-20 06:08:09 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -5.400 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)