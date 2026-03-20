# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_08:05:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,298 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 08:05:16 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.047 |  |
| 2026-03-20 08:04:48 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.096 |  |
| 2026-03-20 08:04:04 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.067 |  |
| 2026-03-20 08:03:53 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-20 08:03:27 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:03:24 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-20 08:03:00 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-20 08:02:58 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:02:49 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.122 |  |
| 2026-03-20 08:01:59 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:01:54 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 08:01:52 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.041 |  |
| 2026-03-20 08:01:52 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-20 08:01:50 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-03-20 08:01:48 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.093 |  |
| 2026-03-20 08:01:38 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-20 08:01:36 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 08:01:21 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:01:03 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-20 08:01:00 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 08:00:47 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:31:19 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-20 07:21:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-20 07:19:16 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:15:01 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:12:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.133 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 07:02:09 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-03-20 02:03:02 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-03-20 07:12:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-20 01:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-20 08:01:38 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-20 08:03:24 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-20 08:01:03 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-20 08:01:52 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-20 08:03:53 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-20 08:01:00 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 07:07:31 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 08:01:54 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 08:01:36 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 08:01:21 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:02:46 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:03:27 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:00:56 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:15:01 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:02:15 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:02:58 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:19:16 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:01:59 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:03:49 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:04:23 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:09:45 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-03-20 07:05:31 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:00:47 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:01:50 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-03-20 08:03:00 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-20 07:07:28 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-03-20 08:01:52 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.041 |  |
| 2026-03-20 08:05:16 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.047 |  |
| 2026-03-20 07:07:53 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.066 |  |
| 2026-03-20 08:04:04 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.067 |  |
| 2026-03-20 08:01:48 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.093 |  |
| 2026-03-20 08:04:48 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.096 |  |
| 2026-03-20 08:02:49 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.122 |  |
| 2026-03-20 07:06:12 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.264 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)