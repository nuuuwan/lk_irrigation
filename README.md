# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_11:07:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,804 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 11:07:43 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-10-02 11:07:31 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:06:57 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-02 11:06:10 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:06:04 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.056 |  |
| 2026-10-02 11:05:05 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:05:03 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 11:04:39 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.411 |  |
| 2026-10-02 11:04:30 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.053 |  |
| 2026-10-02 11:04:26 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-10-02 11:04:22 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.052 |  |
| 2026-10-02 11:04:16 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:03:24 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.011 |  |
| 2026-10-02 11:03:18 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | -0.040 |  |
| 2026-10-02 11:03:18 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:03:09 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-10-02 11:03:01 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:43 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:42 | Nagalagam Street (Kelani Ganga) | 0.29 | 🟢 Normal | -0.031 |  |
| 2026-10-02 11:02:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:26 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.010 |  |
| 2026-10-02 11:02:20 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:19 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:15 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.143 |  |
| 2026-10-02 11:02:07 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.049 |  |
| 2026-10-02 11:01:58 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 11:01:50 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.061 |  |
| 2026-10-02 11:01:48 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:01:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.034 |  |
| 2026-10-02 11:01:24 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:00:52 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:00:51 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:00:45 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.071 |  |
| 2026-10-02 11:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 10:29:12 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 11:06:57 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-02 11:01:58 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 11:05:03 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 11:05:05 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:03:01 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:43 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:01:48 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:19 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:26 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:04:16 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:01:24 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:07:31 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:03:18 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:06:10 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:00:52 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:00:51 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:20 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-02 11:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.010 |  |
| 2026-10-02 10:03:35 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-10-02 11:03:24 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.011 |  |
| 2026-10-02 10:04:20 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-10-02 11:04:26 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-10-02 11:07:43 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-10-02 11:02:42 | Nagalagam Street (Kelani Ganga) | 0.29 | 🟢 Normal | -0.031 |  |
| 2026-10-02 11:03:09 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-10-02 11:01:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.034 |  |
| 2026-10-02 11:03:18 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | -0.040 |  |
| 2026-10-02 10:29:12 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.044 |  |
| 2026-10-02 11:02:07 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.049 |  |
| 2026-10-02 11:04:22 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.052 |  |
| 2026-10-02 11:04:30 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.053 |  |
| 2026-10-02 11:06:04 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.056 |  |
| 2026-10-02 11:01:50 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.061 |  |
| 2026-10-02 11:00:45 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.071 |  |
| 2026-10-02 11:02:15 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.143 |  |
| 2026-10-02 10:00:46 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.399 |  |
| 2026-10-02 11:04:39 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.411 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)