# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_13:17:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,550 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 13:17:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-05 13:12:11 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.052 |  |
| 2026-05-05 13:10:54 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:08:58 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:08:40 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-05-05 13:07:31 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:07:26 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:06:38 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-05-05 13:06:09 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:06:05 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.062 |  |
| 2026-05-05 13:05:51 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-05 13:05:07 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:05:05 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:04:44 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-05 13:04:24 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-05-05 13:03:40 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | -0.120 |  |
| 2026-05-05 13:03:37 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:03:15 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.081 |  |
| 2026-05-05 13:03:14 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.039 |  |
| 2026-05-05 13:03:12 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:02:58 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 13:02:51 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:02:39 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-05 13:02:37 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:02:31 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:02:30 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-05 13:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 13:02:09 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-05 13:02:07 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-05 13:02:07 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-05 13:02:02 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:01:45 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 13:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:01:35 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:01:18 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 13:01:03 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.012 |  |
| 2026-05-05 13:00:53 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 13:17:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-05 13:05:51 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-05 13:02:39 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-05 13:02:07 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-05 13:02:09 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-05 13:01:45 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 13:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 13:01:18 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 13:02:58 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 13:02:31 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:04:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:01:35 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 12:04:42 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:10:54 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:02:37 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:05:05 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:03:37 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:07:31 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:02:51 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:07:26 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:02:02 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:08:58 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:03:12 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:00:53 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:05:07 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:06:09 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 13:06:38 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-05-05 13:04:44 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-05 13:02:07 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-05 13:02:30 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-05 13:08:40 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-05-05 13:01:03 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.012 |  |
| 2026-05-05 13:04:24 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-05-05 13:03:14 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.039 |  |
| 2026-05-05 13:12:11 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.052 |  |
| 2026-05-05 13:06:05 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.062 |  |
| 2026-05-05 13:03:15 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.081 |  |
| 2026-05-05 13:03:40 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)