# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_07:00:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 07:00:37 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:00:30 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.077 |  |
| 2026-02-06 06:47:40 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:39:28 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.007 |  |
| 2026-02-06 06:14:35 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-02-06 06:14:21 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:13:17 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -468.000 |  |
| 2026-02-06 06:13:16 | Padiyathalawa (Maduru Oya) | 1.23 | 🟢 Normal | -468.000 |  |
| 2026-02-06 06:13:14 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -468.000 |  |
| 2026-02-06 06:09:32 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:08:15 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:07:53 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:07:16 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:06:36 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-02-06 06:06:33 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-06 06:06:07 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:05:56 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.077 |  |
| 2026-02-06 06:05:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-06 06:05:34 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-06 06:05:34 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:04:49 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 06:00:27 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-06 06:05:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-06 06:02:18 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-06 06:04:00 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-06 06:05:34 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-06 06:01:50 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 06:04:49 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:06:07 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:03:27 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:03:32 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:14:21 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:01:09 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:02:11 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:07:16 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:07:53 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:09:32 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-06 07:00:37 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:01:06 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:05:34 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:08:15 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-06 06:39:28 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.007 |  |
| 2026-02-06 06:06:36 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-02-06 06:06:33 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-06 06:01:15 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-02-06 06:01:02 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-02-06 06:14:35 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-02-06 06:00:47 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.049 |  |
| 2026-02-06 06:03:42 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-02-06 06:03:44 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.050 |  |
| 2026-02-06 06:04:10 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.057 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 06:01:31 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.072 |  |
| 2026-02-06 07:00:30 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.077 |  |
| 2026-02-06 06:03:42 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.435 |  |
| 2026-02-06 06:13:17 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -468.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)