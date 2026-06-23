# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_15:17:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,281 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 15:17:43 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-06-23 15:13:21 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.046 |  |
| 2026-06-23 15:11:01 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:10:11 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.018 |  |
| 2026-06-23 15:09:45 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.053 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 15:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | 0.000 |  |
| 2026-06-23 15:02:38 | Dunamale (Aththanagalu Oya) | 4.04 | 🟡 Alert | -0.011 |  |
| 2026-06-23 15:01:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-06-23 15:03:52 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-23 15:02:10 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 15:01:18 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:02:00 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:00:47 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:03:25 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:01:47 | Nagalagam Street (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:02:59 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:02:20 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:08:29 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:06:19 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:01:21 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:11:01 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-23 15:17:43 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-06-23 15:05:04 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-23 15:01:05 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-23 15:02:06 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-06-23 15:02:58 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-23 15:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-23 15:01:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.010 |  |
| 2026-06-23 15:01:12 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | -0.010 |  |
| 2026-06-23 15:02:43 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-23 15:10:11 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.018 |  |
| 2026-06-23 15:07:45 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-06-23 15:01:26 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-06-23 15:00:42 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-06-23 15:02:47 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.034 |  |
| 2026-06-23 15:02:26 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.043 |  |
| 2026-06-23 15:13:21 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.046 |  |
| 2026-06-23 15:02:20 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.050 |  |
| 2026-06-23 15:09:45 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.053 |  |
| 2026-06-23 15:02:26 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.085 |  |
| 2026-06-23 15:01:14 | Magura (Kalu Ganga) | 3.15 | 🟢 Normal | -0.093 |  |
| 2026-06-23 15:04:04 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.096 |  |
| 2026-06-23 15:04:01 | Hanwella (Kelani Ganga) | 4.44 | 🟢 Normal | -0.109 |  |
| 2026-06-23 15:08:31 | Glencourse (Kelani Ganga) | 11.67 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)