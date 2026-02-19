# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_00:30:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,714 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 00:30:48 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:23:13 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-20 00:22:00 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-02-20 00:15:57 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-20 00:10:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:09:28 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-20 00:09:17 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:08:38 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:06:50 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:06:40 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:06:32 | Padiyathalawa (Maduru Oya) | 3.75 | 🟢 Normal | -0.348 |  |
| 2026-02-20 00:06:26 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 864.000 | 🔺 Rising |
| 2026-02-20 00:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 864.000 | 🔺 Rising |
| 2026-02-20 00:06:22 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-02-20 00:05:55 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-02-20 00:04:54 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-20 00:04:40 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 00:04:31 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:04:11 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:04:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 00:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 864.000 | 🔺 Rising |
| 2026-02-20 00:22:00 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-02-19 18:04:32 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-20 00:03:32 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 00:09:28 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-20 00:03:29 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-20 00:02:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 00:23:13 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-20 00:04:40 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 00:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 00:15:57 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-20 00:02:45 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:06:40 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:30:48 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:04:11 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:02:27 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:04:31 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 23:12:07 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:02:12 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:09:17 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:10:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:02:03 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:08:38 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:06:26 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:06:50 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:03:54 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:01:54 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-19 22:05:19 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:04:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:02:00 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-20 00:06:22 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-02-20 00:04:54 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-20 00:03:05 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-20 00:05:55 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-02-20 00:02:22 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | -0.059 |  |
| 2026-02-19 23:04:35 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.125 |  |
| 2026-02-20 00:06:32 | Padiyathalawa (Maduru Oya) | 3.75 | 🟢 Normal | -0.348 |  |
| 2026-02-20 00:01:47 | Wellawaya (Kirindi Oya) | 0.12 | 🟢 Normal | -0.823 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)