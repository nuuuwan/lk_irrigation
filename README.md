# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_17:29:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,746 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 17:29:50 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.007 |  |
| 2026-02-26 17:15:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:09:38 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-26 17:08:11 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:07:56 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-26 17:07:56 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-26 17:07:43 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-02-26 17:06:07 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:05:53 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-02-26 17:05:42 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:05:04 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:04:52 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:04:28 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:04:26 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:03:51 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:03:46 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:03:13 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-02-26 17:03:08 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-02-26 17:02:53 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:46 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:40 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-02-26 17:02:38 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:35 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:31 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:18 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-02-26 17:02:11 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:11 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:08 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:07 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:05 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-26 17:01:55 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-02-26 17:01:53 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-26 17:01:51 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-26 17:01:43 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:01:40 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-02-26 17:01:39 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:01:19 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-26 17:01:17 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:00:17 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.110 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 17:02:05 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-26 17:09:38 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-26 17:01:51 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-26 17:07:56 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-26 17:01:53 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-26 17:02:08 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:03:51 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:15:57 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:01:43 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:31 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:35 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:04:28 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:46 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:05:04 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:06:07 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:08:11 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:01:39 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:38 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:53 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:11 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:04:26 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:05:42 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:18 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:03:46 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:04:52 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:01:17 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:02:11 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 17:29:50 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.007 |  |
| 2026-02-26 17:05:53 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-02-26 17:07:56 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-26 17:01:55 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-02-26 17:01:40 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-02-26 17:02:40 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-02-26 17:07:43 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-02-26 17:03:08 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-02-26 17:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-02-26 17:01:19 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-26 17:03:13 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-02-26 17:00:17 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)