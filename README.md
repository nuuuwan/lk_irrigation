# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_01:31:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 01:31:17 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:14:14 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.903 | 🔺 Rising |
| 2026-04-16 01:10:33 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-16 01:07:34 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:07:11 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-04-16 01:06:43 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:06:35 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:05:33 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:04:28 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:03:34 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-04-16 01:03:00 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 01:02:37 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:02:19 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-16 01:02:10 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 8.690 | 🔺 Rising |
| 2026-04-16 01:02:08 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:02:00 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.044 |  |
| 2026-04-16 01:01:58 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-16 01:01:48 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 01:01:43 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-16 01:01:41 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 8.690 | 🔺 Rising |
| 2026-04-16 01:01:41 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:01:40 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 8.690 | 🔺 Rising |
| 2026-04-16 01:01:39 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:01:35 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-16 01:01:09 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-04-16 01:01:06 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-16 01:00:55 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.169 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 01:02:10 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 8.690 | 🔺 Rising |
| 2026-04-16 00:24:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 2.700 | 🔺 Rising |
| 2026-04-16 01:14:14 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.903 | 🔺 Rising |
| 2026-04-16 01:01:58 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-16 00:03:09 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-16 00:09:08 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-16 01:10:33 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-16 01:02:19 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-16 01:01:48 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 22:13:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-16 01:01:35 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-16 01:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 01:06:35 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:03:00 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:01:48 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:05:33 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:07:34 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:02:37 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:31:17 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:01:39 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:01:41 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:04:28 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:02:08 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:06:43 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:05:34 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:07:11 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-04-16 00:03:47 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-16 01:01:06 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-16 01:01:43 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-16 01:01:09 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-04-16 00:04:40 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.012 |  |
| 2026-04-16 01:03:34 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-16 01:02:00 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.044 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-16 01:00:55 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.169 |  |
| 2026-04-16 00:00:12 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.240 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)