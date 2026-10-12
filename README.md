# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_12:10:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,840 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 12:10:17 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-12 12:09:15 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.063 |  |
| 2026-10-12 12:09:11 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:07:28 | Glencourse (Kelani Ganga) | 11.14 | 🟢 Normal | -0.029 |  |
| 2026-10-12 12:06:45 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.011 |  |
| 2026-10-12 12:06:12 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.060 |  |
| 2026-10-12 12:05:40 | Rathnapura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.129 |  |
| 2026-10-12 12:05:03 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.066 |  |
| 2026-10-12 12:04:52 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:04:46 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:04:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:03:58 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-12 12:03:55 | Ellagawa (Kalu Ganga) | 7.23 | 🟢 Normal | -0.030 |  |
| 2026-10-12 12:03:45 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:03:19 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:03:17 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:03:06 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.088 |  |
| 2026-10-12 12:03:04 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:03:00 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-10-12 12:03:00 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-10-12 12:02:45 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:02:43 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-12 12:02:40 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-12 12:02:37 | Giriulla (Maha Oya) | 2.17 | 🟢 Normal | -0.075 |  |
| 2026-10-12 12:02:27 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-10-12 12:02:23 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.081 |  |
| 2026-10-12 12:02:15 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:02:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-12 12:02:08 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:02:07 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-12 12:02:06 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | -0.043 |  |
| 2026-10-12 12:01:48 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:01:36 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-10-12 12:01:28 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.131 |  |
| 2026-10-12 12:01:24 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.022 |  |
| 2026-10-12 12:01:19 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 12:01:19 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-12 12:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-10-12 12:00:49 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.107 |  |
| 2026-10-12 12:00:06 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:59:27 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 12:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-10-12 12:02:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-12 12:01:19 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 12:00:06 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:02:15 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:02:08 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:02:45 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:04:46 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:03:00 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:03:04 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:09:11 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:04:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:03:19 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:03:17 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:03:45 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:01:19 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-12 12:10:17 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-12 12:02:07 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-12 12:02:40 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-12 12:03:58 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-12 12:06:45 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.011 |  |
| 2026-10-12 12:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-10-12 12:02:43 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-12 12:03:00 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-10-12 12:01:24 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.022 |  |
| 2026-10-12 12:07:28 | Glencourse (Kelani Ganga) | 11.14 | 🟢 Normal | -0.029 |  |
| 2026-10-12 12:03:55 | Ellagawa (Kalu Ganga) | 7.23 | 🟢 Normal | -0.030 |  |
| 2026-10-12 12:02:27 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-10-12 12:02:06 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | -0.043 |  |
| 2026-10-12 12:01:36 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-10-12 12:06:12 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.060 |  |
| 2026-10-12 12:09:15 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.063 |  |
| 2026-10-12 12:05:03 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.066 |  |
| 2026-10-12 12:02:37 | Giriulla (Maha Oya) | 2.17 | 🟢 Normal | -0.075 |  |
| 2026-10-12 12:02:23 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.081 |  |
| 2026-10-12 12:03:06 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.088 |  |
| 2026-10-12 12:00:49 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.107 |  |
| 2026-10-12 12:05:40 | Rathnapura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.129 |  |
| 2026-10-12 12:01:28 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)