# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_07:07:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,801 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 07:07:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.027 |  |
| 2026-03-15 07:07:40 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.045 |  |
| 2026-03-15 07:07:09 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:06:46 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:06:31 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:05:27 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:05:24 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:05:23 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-03-15 07:05:06 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-03-15 07:04:43 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-15 07:03:52 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:03:49 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:03:48 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-15 07:03:44 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-15 07:03:36 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:03:22 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 07:03:17 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:03:02 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-03-15 07:02:55 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:02:49 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-03-15 07:02:47 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-15 07:02:31 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-15 07:02:22 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-15 07:02:20 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.121 |  |
| 2026-03-15 07:01:28 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:01:20 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:01:20 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.042 |  |
| 2026-03-15 07:01:19 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.087 |  |
| 2026-03-15 07:01:17 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:01:12 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.099 |  |
| 2026-03-15 07:01:10 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:01:05 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-03-15 07:01:04 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 07:00:56 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.003 |  |
| 2026-03-15 07:00:19 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-03-15 07:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-15 06:28:57 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-15 06:15:41 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 07:02:22 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-15 07:03:48 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-15 06:07:45 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 07:03:44 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-15 07:03:22 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 07:04:43 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-15 07:02:47 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-15 06:03:26 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-15 07:01:04 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 07:00:56 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.003 |  |
| 2026-03-15 07:06:46 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:05:27 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:06:31 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:01:28 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:03:52 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:01:20 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:03:36 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:03:17 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:01:17 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:07:09 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:03:49 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:05:24 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:01:10 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:02:49 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-03-15 06:05:58 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-15 07:02:31 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-15 07:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-15 07:01:05 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-03-15 07:05:06 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-03-15 06:08:06 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-15 07:05:23 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-03-15 07:03:02 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-03-15 07:07:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.027 |  |
| 2026-03-15 07:01:20 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.042 |  |
| 2026-03-15 07:07:40 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.045 |  |
| 2026-03-15 07:00:19 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-03-15 07:01:19 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.087 |  |
| 2026-03-15 07:01:12 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.099 |  |
| 2026-03-15 07:02:20 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)