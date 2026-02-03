# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--03_08:06:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,102 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 08:06:14 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.084 |  |
| 2026-02-03 08:06:01 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-02-03 08:05:51 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-03 08:04:51 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-02-03 08:03:51 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-03 08:03:26 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:03:23 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:03:16 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-03 08:02:51 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:02:41 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:02:41 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-02-03 08:02:29 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.157 |  |
| 2026-02-03 08:02:21 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.039 |  |
| 2026-02-03 08:02:05 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-03 08:02:01 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -18.000 |  |
| 2026-02-03 08:01:59 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -18.000 |  |
| 2026-02-03 08:01:45 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:01:23 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.060 |  |
| 2026-02-03 08:01:21 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.022 |  |
| 2026-02-03 08:00:47 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:00:37 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:37:54 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-03 07:16:38 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:13 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-03 07:13:11 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-03 07:11:55 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-03 07:11:35 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:11:19 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 05:18:55 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-03 07:00:09 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-03 08:03:16 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-03 08:05:51 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-03 05:03:58 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-03 07:37:54 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-03 08:03:51 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-03 08:02:41 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:00:37 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:00:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:16:38 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:03:26 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:01:45 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:00:47 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:02:51 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:11:35 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:08:33 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:07:05 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-03 08:03:23 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-03 08:04:51 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-02-03 08:02:05 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-03 06:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-03 07:03:48 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-02-03 07:01:30 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.012 |  |
| 2026-02-03 08:06:01 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 08:01:21 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.022 |  |
| 2026-02-03 08:02:41 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-02-03 08:02:21 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.039 |  |
| 2026-02-03 08:01:23 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.060 |  |
| 2026-02-03 06:04:03 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.064 |  |
| 2026-02-03 05:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 08:06:14 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.084 |  |
| 2026-02-03 08:02:29 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.157 |  |
| 2026-02-03 06:01:58 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.197 |  |
| 2026-02-03 08:02:01 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)