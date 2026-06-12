# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_22:22:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,726 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 22:22:06 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-12 22:11:55 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:10:28 | Rathnapura (Kalu Ganga) | 6.59 | 🟡 Alert | -0.120 |  |
| 2026-06-12 22:09:56 | Holombuwa (Kelani Ganga) | 1.64 | 🟢 Normal | -0.079 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 22:05:26 | Magura (Kalu Ganga) | 4.70 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-06-12 22:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.000 |  |
| 2026-06-12 22:10:28 | Rathnapura (Kalu Ganga) | 6.59 | 🟡 Alert | -0.120 |  |
| 2026-06-12 22:05:59 | Peradeniya (Mahaweli Ganga) | 3.11 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-06-12 22:06:08 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-06-12 22:06:40 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-06-12 22:06:28 | Urawa (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-12 22:02:49 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-12 22:22:06 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-12 22:06:30 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 22:01:45 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 22:04:27 | Baddegama (Gin Ganga) | 2.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 22:02:35 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 22:02:29 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 22:03:57 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 22:04:37 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 22:04:16 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:00:27 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:07:38 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:01:31 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:00:38 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:03:48 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:04:06 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:01:37 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:02:41 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:11:55 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:01:52 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:05:21 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-12 22:05:58 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | -0.009 |  |
| 2026-06-12 22:03:01 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-12 22:03:02 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-12 22:03:46 | Norwood (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-06-12 22:03:02 | Giriulla (Maha Oya) | 2.36 | 🟢 Normal | -0.030 |  |
| 2026-06-12 22:09:56 | Holombuwa (Kelani Ganga) | 1.64 | 🟢 Normal | -0.079 |  |
| 2026-06-12 21:02:52 | Nawalapitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.113 |  |
| 2026-06-12 22:02:30 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)