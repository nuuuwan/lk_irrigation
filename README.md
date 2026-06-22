# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_18:00:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,464 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 18:00:34 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-22 18:00:15 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:00:09 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-22 17:13:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:11:53 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 17:10:00 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 17:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-06-22 17:09:10 | Magura (Kalu Ganga) | 3.00 | 🟢 Normal | 0.922 | 🔺 Rising |
| 2026-06-22 17:04:35 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-06-22 17:03:31 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-22 17:06:18 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-22 17:04:25 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-22 17:07:45 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-22 17:05:57 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-22 17:04:00 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-22 17:07:11 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-22 18:00:09 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-22 17:00:36 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-22 17:01:22 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-22 17:04:13 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-22 17:02:55 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 17:06:58 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-22 17:11:53 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 17:05:15 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 17:03:50 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:04:27 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:03:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:00:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:13:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:04:21 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:03:21 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:02:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:05:30 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:04:22 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:01:44 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:08:50 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:00:15 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:01:38 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 17:03:02 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:00:34 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-22 17:05:18 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-06-22 17:00:34 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-06-22 17:10:00 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-06-22 17:00:26 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.040 |  |
| 2026-06-22 17:03:47 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)