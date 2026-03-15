# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_08:06:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,834 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 08:06:36 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-03-15 08:06:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:06:23 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:06:19 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:06:16 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.131 |  |
| 2026-03-15 08:05:41 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-03-15 08:05:40 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:05:14 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:04:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.063 |  |
| 2026-03-15 08:03:47 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:03:37 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-15 08:03:19 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:02:58 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-15 08:02:43 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-03-15 08:02:35 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | -0.052 |  |
| 2026-03-15 08:02:27 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:02:15 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:02:12 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:02:08 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.020 |  |
| 2026-03-15 08:01:52 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.149 |  |
| 2026-03-15 08:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-03-15 08:01:19 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 08:01:18 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.050 |  |
| 2026-03-15 08:01:11 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:01:11 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:01:11 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:01:09 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:01:01 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:00:12 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-15 07:42:40 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-03-15 07:20:48 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 07:13:18 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 07:12:26 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 08:06:36 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-03-15 07:03:44 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-15 07:03:22 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 08:03:37 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-15 07:04:43 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-15 07:13:18 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 08:01:19 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 08:03:47 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:06:19 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:03:19 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:01:09 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:02:15 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:01:01 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:05:14 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:01:11 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:02:12 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:06:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:06:23 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:02:27 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:01:11 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:05:40 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:01:11 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 08:02:58 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-15 08:00:12 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-15 08:02:43 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-03-15 08:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-03-15 08:02:08 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.020 |  |
| 2026-03-15 07:03:02 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-03-15 08:05:41 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-03-15 07:42:40 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-03-15 07:07:40 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.045 |  |
| 2026-03-15 08:01:18 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.050 |  |
| 2026-03-15 08:02:35 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | -0.052 |  |
| 2026-03-15 07:00:19 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-03-15 08:04:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.063 |  |
| 2026-03-15 07:01:19 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.087 |  |
| 2026-03-15 07:02:20 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.121 |  |
| 2026-03-15 08:06:16 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.131 |  |
| 2026-03-15 08:01:52 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)