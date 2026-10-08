# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_06:33:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,013 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 06:33:04 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | -0.002 |  |
| 2026-10-08 06:13:02 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-08 06:08:31 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -12.000 |  |
| 2026-10-08 06:08:13 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -12.000 |  |
| 2026-10-08 06:07:38 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.084 |  |
| 2026-10-08 06:07:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2026-10-08 06:06:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 06:05:44 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-10-08 06:05:33 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | 0.411 | 🔺 Rising |
| 2026-10-08 06:05:15 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.042 |  |
| 2026-10-08 06:04:55 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-08 06:04:02 | Dunamale (Aththanagalu Oya) | 2.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 06:03:59 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-10-08 06:03:53 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-10-08 06:03:52 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-08 06:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-10-08 06:03:40 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-10-08 06:03:21 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.769 |  |
| 2026-10-08 06:03:06 | Giriulla (Maha Oya) | 2.84 | 🟢 Normal | -0.111 |  |
| 2026-10-08 06:02:45 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.139 |  |
| 2026-10-08 06:02:44 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-10-08 06:02:43 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 06:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 0.448 | 🔺 Rising |
| 2026-10-08 06:05:33 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | 0.411 | 🔺 Rising |
| 2026-10-08 06:00:16 | Moragaswewa (Deduru Oya) | 0.74 | 🟢 Normal | 0.370 | 🔺 Rising |
| 2026-10-08 06:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-10-08 06:02:23 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-08 06:13:02 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-08 06:01:22 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 06:04:02 | Dunamale (Aththanagalu Oya) | 2.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 06:01:03 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-08 06:06:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 06:01:44 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 06:01:34 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-08 06:01:30 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 06:01:16 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-08 06:03:52 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-08 06:02:43 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 06:04:55 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-08 06:02:39 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:09:53 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-08 06:33:04 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | -0.002 |  |
| 2026-10-08 06:02:00 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-08 06:05:44 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-10-08 06:02:44 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-10-08 06:03:59 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-10-08 06:01:59 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-10-08 06:03:53 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-10-08 06:03:40 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-10-08 06:05:15 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.042 |  |
| 2026-10-08 06:00:11 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.047 |  |
| 2026-10-08 06:01:16 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.051 |  |
| 2026-10-08 06:07:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2026-10-08 06:01:33 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | -0.072 |  |
| 2026-10-08 06:01:45 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.072 |  |
| 2026-10-08 06:02:34 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -0.080 |  |
| 2026-10-08 06:07:38 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.084 |  |
| 2026-10-08 06:03:06 | Giriulla (Maha Oya) | 2.84 | 🟢 Normal | -0.111 |  |
| 2026-10-08 06:02:45 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.139 |  |
| 2026-10-08 06:03:21 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.769 |  |
| 2026-10-08 06:08:31 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -12.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)