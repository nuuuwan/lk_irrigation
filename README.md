# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_09:09:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,883 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 09:09:53 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.215 |  |
| 2026-03-15 09:08:04 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | -0.046 |  |
| 2026-03-15 09:06:12 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.019 |  |
| 2026-03-15 09:06:11 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-15 09:06:08 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-15 09:05:58 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.061 |  |
| 2026-03-15 09:05:53 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:05:37 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-03-15 09:05:10 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.028 |  |
| 2026-03-15 09:04:57 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-15 09:04:17 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:04:17 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-15 09:04:07 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:41 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:40 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:16 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-15 09:03:11 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:08 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:02 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.085 |  |
| 2026-03-15 09:03:01 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:02:53 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-03-15 09:02:49 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.236 |  |
| 2026-03-15 09:02:45 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:02:43 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:02:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-03-15 09:02:26 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:02:23 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-03-15 09:02:19 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.036 |  |
| 2026-03-15 09:02:18 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:02:14 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:01:59 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 09:01:59 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -36.000 |  |
| 2026-03-15 09:01:58 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -36.000 |  |
| 2026-03-15 09:01:43 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.047 |  |
| 2026-03-15 09:01:42 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:01:40 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:01:18 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:01:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.085 |  |
| 2026-03-15 09:00:52 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:00:15 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 09:02:23 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-03-15 09:04:57 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-15 09:06:08 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-15 09:01:59 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 09:02:26 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:01:18 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:01 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:02:14 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:02:45 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:02:18 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:02:43 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:40 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:08 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:04:07 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:01:40 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:41 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:11 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:00:52 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:05:53 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:04:17 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:01:42 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 09:03:16 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-15 09:05:37 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-03-15 09:06:11 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-15 09:04:17 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-15 09:06:12 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.019 |  |
| 2026-03-15 09:02:53 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-03-15 09:02:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-03-15 09:05:10 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.028 |  |
| 2026-03-15 09:02:19 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.036 |  |
| 2026-03-15 09:08:04 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | -0.046 |  |
| 2026-03-15 09:01:43 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.047 |  |
| 2026-03-15 09:05:58 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.061 |  |
| 2026-03-15 09:00:15 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.071 |  |
| 2026-03-15 09:03:02 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.085 |  |
| 2026-03-15 09:01:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.085 |  |
| 2026-03-15 09:09:53 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.215 |  |
| 2026-03-15 09:02:49 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.236 |  |
| 2026-03-15 09:01:59 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)