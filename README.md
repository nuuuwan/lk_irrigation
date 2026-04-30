# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_18:18:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,316 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 18:18:16 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:12:40 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.017 |  |
| 2026-04-30 18:11:28 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-30 18:09:27 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:08:58 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.086 |  |
| 2026-04-30 18:08:37 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.048 |  |
| 2026-04-30 18:07:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.129 |  |
| 2026-04-30 18:06:09 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:05:55 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:05:52 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:05:49 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:05:09 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-30 18:04:37 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-04-30 18:04:18 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 18:03:55 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:03:52 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:03:27 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:07 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-04-30 18:03:06 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:02:55 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:33 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.021 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:28 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:20 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.061 |  |
| 2026-04-30 18:02:18 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.021 |  |
| 2026-04-30 18:02:03 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:01:55 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:01:51 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.081 |  |
| 2026-04-30 18:01:47 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:01:25 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:01:12 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.012 |  |
| 2026-04-30 18:01:08 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:01:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.031 |  |
| 2026-04-30 18:00:33 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:00:33 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.083 |  |
| 2026-04-30 18:00:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:56:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 18:04:37 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-04-30 18:05:09 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-30 18:03:27 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 18:04:18 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 18:11:28 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-30 18:00:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:09:27 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:01:55 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:05:55 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:01:08 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:05:52 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:03 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:06:09 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:03:52 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:03:55 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:55 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:28 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:18:16 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:00:33 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:03:06 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:05:49 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:01:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:01:47 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:01:12 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.012 |  |
| 2026-04-30 18:12:40 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.017 |  |
| 2026-04-30 18:02:18 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.021 |  |
| 2026-04-30 18:02:33 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.021 |  |
| 2026-04-30 18:03:07 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-04-30 18:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.031 |  |
| 2026-04-30 17:56:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.032 |  |
| 2026-04-30 18:08:37 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.048 |  |
| 2026-04-30 18:02:20 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.061 |  |
| 2026-04-30 18:01:51 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.081 |  |
| 2026-04-30 18:00:33 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.083 |  |
| 2026-04-30 18:08:58 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.086 |  |
| 2026-04-30 18:07:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)